from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from app.core.database import get_db
from app.models import Sentence as SentenceModel
from app.schemas import Sentence as SentenceSchema, SentenceCreate

router = APIRouter()


@router.get("/random", response_model=SentenceSchema)
def get_random_sentence(
    level: Optional[str] = Query(default="B2", max_length=5),
    category: Optional[str] = Query(default=None, max_length=50),
    db: Session = Depends(get_db),
):
    query = db.query(SentenceModel)
    if level:
        query = query.filter(func.upper(SentenceModel.level) == level.upper())
    if category:
        query = query.filter(func.upper(SentenceModel.category) == category.upper())

    sentence = query.order_by(func.random()).first()
    if not sentence:
        raise HTTPException(status_code=404, detail="No sentences found for this level and category")
    return sentence


@router.get("", response_model=List[SentenceSchema])
def get_sentences(
    level: Optional[str] = Query(default=None, max_length=5),
    category: Optional[str] = Query(default=None, max_length=50),
    limit: int = Query(default=100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    query = db.query(SentenceModel)
    if level:
        query = query.filter(func.upper(SentenceModel.level) == level.upper())
    if category:
        query = query.filter(func.upper(SentenceModel.category) == category.upper())
    return query.order_by(SentenceModel.id.asc()).limit(limit).all()


@router.post("", response_model=SentenceSchema)
def create_sentence(sentence: SentenceCreate, db: Session = Depends(get_db)):
    payload = sentence.model_dump() if hasattr(sentence, "model_dump") else sentence.dict()
    db_sentence = SentenceModel(**payload)
    db.add(db_sentence)
    db.commit()
    db.refresh(db_sentence)
    return db_sentence
