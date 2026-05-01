from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..core.database import get_db
from ..models import Sentence

router = APIRouter()

@router.get("", response_model=List[str])
def get_categories(db: Session = Depends(get_db)):
    """Get all available sentence categories"""
    categories = db.query(Sentence.category).distinct().order_by(Sentence.category).all()
    return [cat[0] for cat in categories if cat[0]]