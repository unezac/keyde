from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import Sentence

router = APIRouter()


@router.get("", response_model=List[str])
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Sentence.category).distinct().order_by(Sentence.category).all()
    return [cat[0] for cat in categories if cat[0]]
