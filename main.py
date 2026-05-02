from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_db, reset_database, ensure_database, add_missing_columns
from app.routes import sentences, categories, levels
from app.models import Sentence

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="KeyGermany API",
    description="German typing practice sentences with English and Arabic translations.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

static_dir = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.on_event("startup")
def startup_event():
    add_missing_columns()
    result = ensure_database()

    if result.get("created") or result.get("status") == "ok":
        from sqlalchemy.orm import Session
        from app.core.database import SessionLocal

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
                        category="Daily Life",
                    ),
                    Sentence(
                        german_text="Ich möchte einen Kaffee trinken und ein Stück Kuchen essen.",
                        english_translation="I would like to drink a coffee and eat a piece of cake.",
                        arabic_translation="أود أن أشرب قهوة وأكل قطعة كعك.",
                        level="B2",
                        difficulty_score=4,
                        category="Food & Drinks",
                    ),
                    Sentence(
                        german_text="Die Bücher in der Bibliothek sind sehr interessant und lehrreich.",
                        english_translation="The books in the library are very interesting and educational.",
                        arabic_translation="الكتب في المكتبة مثيرة جداً وتعليمية.",
                        level="B2",
                        difficulty_score=6,
                        category="Education",
                    ),
                ]
                for sentence in sample_sentences:
                    db.add(sentence)
                db.commit()
        finally:
            db.close()


app.include_router(sentences.router, prefix="/api/sentences", tags=["sentences"])
app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
app.include_router(levels.router, prefix="/api/levels", tags=["levels"])


@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "KeyGermany API"}


@app.get("/", response_class=HTMLResponse)
def root():
    index_path = static_dir / "index.html"
    if index_path.exists():
        return index_path.read_text(encoding="utf-8")
    return HTMLResponse("<h1>Welcome to KeyGermany</h1><p>Static files not found.</p>")
