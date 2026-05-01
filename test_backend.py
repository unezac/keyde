import sys
import os

# Add the current directory to sys.path to simulate running from root
sys.path.append(os.getcwd())

try:
    print("Testing imports...")
    from backend.app.models import Sentence
    print("Successfully imported Sentence from backend.app.models")
    
    from backend.app.main import app
    print("Successfully imported FastAPI app from backend.app.main")
    
    from backend.app.core.database import ensure_database
    print("Running ensure_database()...")
    result = ensure_database()
    print(f"Database status: {result}")
    
    print("\nSUCCESS: All critical components imported and database check passed.")
except Exception as e:
    print(f"\nFAILURE: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
