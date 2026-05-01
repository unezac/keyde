import os
from pathlib import Path

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[3]
BACKEND_ROOT = Path(__file__).resolve().parents[2]

load_dotenv(PROJECT_ROOT / ".env")
load_dotenv(BACKEND_ROOT / ".env")

# Use SQLite for development, PostgreSQL for production
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    # SQLite for local development. Vercel serverless functions can write only
    # to /tmp, so use an ephemeral DB there unless DATABASE_URL is configured.
    if os.getenv("VERCEL"):
        abs_path = Path("/tmp/keygermany.db")
    else:
        abs_path = BACKEND_ROOT / "keygermany.db"
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{abs_path}"
    DB_FILE_PATH = abs_path
else:
    SQLALCHEMY_DATABASE_URL = DATABASE_URL
    DB_FILE_PATH = None

# SQLite requires check_same_thread=False
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Create all tables in the database"""
    Base.metadata.create_all(bind=engine)


def reset_database():
    """
    Fully automated database reset + recreate system.
    
    1. Detects if keygermany.db exists
    2. Deletes the old database automatically using Python (os.remove)
    3. Recreates a brand new database automatically
    4. Uses SQLAlchemy Base.metadata.create_all(bind=engine)
    5. Ensures all tables and columns are rebuilt correctly
    
    Returns: dict with status and details
    """
    result = {"action": "reset_database", "deleted": False, "created": False, "tables": []}
    
    # Also dispose engine connections to ensure clean slate
    engine.dispose()
    
    # Step 1: Detect if database file exists and delete it
    if DB_FILE_PATH and DB_FILE_PATH.exists():
        try:
            os.remove(DB_FILE_PATH)
            result["deleted"] = True
            result["deleted_file"] = str(DB_FILE_PATH)
        except Exception as e:
            return {"status": "error", "message": f"Failed to delete database: {e}", **result}
    
    # Step 2: Recreate database and all tables
    try:
        Base.metadata.create_all(bind=engine)
        result["created"] = True
        
        # Step 3: Verify all tables were created with correct columns
        inspector = inspect(engine)
        for table_name in Base.metadata.tables:
            columns = inspector.get_columns(table_name)
            result["tables"].append({
                "table": table_name,
                "columns": [col["name"] for col in columns]
            })
        
        result["status"] = "success"
        result["message"] = "Database reset and recreated successfully"
        return result
    except Exception as e:
        return {"status": "error", "message": f"Failed to create tables: {e}", **result}


def check_schema():
    """
    Check if the database schema matches the expected models.
    Returns True if schema is valid, False if mismatch or missing.
    """
    try:
        inspector = inspect(engine)
        
        # Check if all expected tables exist
        expected_tables = set(Base.metadata.tables.keys())
        existing_tables = set(inspector.get_table_names())
        
        if not expected_tables.issubset(existing_tables):
            return False
        
        # Check if Sentence table has all expected columns
        if "sentences" in existing_tables:
            columns = inspector.get_columns("sentences")
            column_names = {col["name"] for col in columns}
            expected_columns = {
                "id", "german_text", "english_translation", 
                "arabic_translation", "level", "difficulty_score",
                "category", "created_at", "updated_at"
            }
            if not expected_columns.issubset(column_names):
                return False
        
        return True
    except Exception:
        return False


def add_missing_columns():
    """
    Add missing columns to existing tables without deleting data.
    This runs during startup to handle database migrations.
    """
    from sqlalchemy import text
    
    inspector = inspect(engine)
    
    try:
        if "sentences" in inspector.get_table_names():
            columns = inspector.get_columns("sentences")
            column_names = {col["name"] for col in columns}
            
            # Check if 'category' column exists, if not, add it
            if "category" not in column_names:
                with engine.begin() as connection:
                    if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
                        connection.execute(
                            text('ALTER TABLE sentences ADD COLUMN category VARCHAR(50) DEFAULT "Daily Life"')
                        )
                    else:
                        connection.execute(
                            text('ALTER TABLE sentences ADD COLUMN category VARCHAR(50) DEFAULT \'Daily Life\'')
                        )
                print("✓ Added 'category' column to sentences table")
            
            return {"status": "success", "message": "Schema migration completed"}
    except Exception as e:
        print(f"✗ Migration error: {e}")
        return {"status": "error", "message": str(e)}


def ensure_database():
    """
    Ensures database exists and schema is correct.
    Resets and rebuilds automatically if schema mismatch detected.
    Returns the result dict.
    """
    if not check_schema():
        return reset_database()
    return {"status": "ok", "message": "Database schema is valid, no action needed"}
