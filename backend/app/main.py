from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.database import init_db, reset_database, ensure_database
from .routes import sentences, categories, levels

app = FastAPI(
    title="KeyGermany API",
    description="German typing practice sentences with English and Arabic translations.",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    """Initialize database: create DB if first run, handle schema migrations"""
    from .models import Sentence
    from .core.database import add_missing_columns
    
    # Run schema migrations first (adds missing columns without deleting data)
    add_missing_columns()
    
    # Ensure database exists and schema is valid
    result = ensure_database()
    
    # Seed database with sample data if it was created or is empty
    if result.get("created") or result.get("status") == "ok":
        from sqlalchemy.orm import Session
        from .core.database import SessionLocal
        
        db = SessionLocal()
        try:
            count = db.query(Sentence).count()
            if count == 0:
                sample_sentences = [
                    Sentence(
                        german_text="Der schnelle braune Fuchs springt über den faulen Hund.",
                        english_translation="The quick brown fox jumps over the lazy dog.",
                        arabic_translation="الثعلب البني السريع يقفز فوق الكلب الكسول.",
                        level="B2",
                        difficulty_score=5,
                        category="Daily Life"
                    ),
                    Sentence(
                        german_text="Ich möchte einen Kaffee trinken und ein Stück Kuchen essen.",
                        english_translation="I would like to drink a coffee and eat a piece of cake.",
                        arabic_translation="أود أن أشرب قهوة وأكل قطعة كعك.",
                        level="B2",
                        difficulty_score=4,
                        category="Food & Drinks"
                    ),
                    Sentence(
                        german_text="Die Bücher in der Bibliothek sind sehr interessant und lehrreich.",
                        english_translation="The books in the library are very interesting and educational.",
                        arabic_translation="الكتب في المكتبة مثيرة جداً وتعليمية.",
                        level="B2",
                        difficulty_score=6,
                        category="Education"
                    ),
                ]
                for sentence in sample_sentences:
                    db.add(sentence)
                db.commit()
        finally:
            db.close()

# Include routers
app.include_router(sentences.router, prefix="/api/sentences", tags=["sentences"])
app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
app.include_router(levels.router, prefix="/api/levels", tags=["levels"])

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "KeyGermany API"}

@app.get("/")
def root():
    return {
        "message": "KeyGermany API",
        "docs": "http://127.0.0.1:8000/docs",
        "endpoints": {
            "health": "/api/health",
            "random_sentence": "/api/sentences/random",
            "all_sentences": "/api/sentences",
            "create_sentence": "/api/sentences (POST)",
            "categories": "/api/categories",
            "levels": "/api/levels"
        }
    }