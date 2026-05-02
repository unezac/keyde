import os
from pathlib import Path

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]

load_dotenv(PROJECT_ROOT / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    abs_path = PROJECT_ROOT / "keygermany.db"
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{abs_path}"
    DB_FILE_PATH = abs_path
else:
    SQLALCHEMY_DATABASE_URL = DATABASE_URL
    DB_FILE_PATH = None

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
    Base.metadata.create_all(bind=engine)


def reset_database():
    result = {"action": "reset_database", "deleted": False, "created": False, "tables": []}

    engine.dispose()

    if DB_FILE_PATH and DB_FILE_PATH.exists():
        try:
            os.remove(DB_FILE_PATH)
            result["deleted"] = True
            result["deleted_file"] = str(DB_FILE_PATH)
        except Exception as e:
            return {"status": "error", "message": f"Failed to delete database: {e}", **result}

    try:
        Base.metadata.create_all(bind=engine)
        result["created"] = True

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
    try:
        inspector = inspect(engine)

        expected_tables = set(Base.metadata.tables.keys())
        existing_tables = set(inspector.get_table_names())

        if not expected_tables.issubset(existing_tables):
            return False

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
    from sqlalchemy import text

    inspector = inspect(engine)

    try:
        if "sentences" in inspector.get_table_names():
            columns = inspector.get_columns("sentences")
            column_names = {col["name"] for col in columns}

            if "category" not in column_names:
                with engine.begin() as connection:
                    if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
                        connection.execute(
                            text('ALTER TABLE sentences ADD COLUMN category VARCHAR(50) DEFAULT "Daily Life"')
                        )
                    else:
                        connection.execute(
                            text("ALTER TABLE sentences ADD COLUMN category VARCHAR(50) DEFAULT 'Daily Life'")
                        )
                print("Added 'category' column to sentences table")

            return {"status": "success", "message": "Schema migration completed"}
    except Exception as e:
        print(f"Migration error: {e}")
        return {"status": "error", "message": str(e)}


def ensure_database():
    if not check_schema():
        return reset_database()
    return {"status": "ok", "message": "Database schema is valid, no action needed"}
