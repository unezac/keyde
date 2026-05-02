from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import Sentence

router = APIRouter()


@router.get("", response_model=List[str])
def get_levels(db: Session = Depends(get_db)):
    levels = db.query(Sentence.level).distinct().order_by(Sentence.level).all()
    return [level[0] for level in levels if level[0]]
