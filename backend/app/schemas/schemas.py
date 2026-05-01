from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class SentenceBase(BaseModel):
    german_text: str
    english_translation: str
    arabic_translation: str
    level: Optional[str] = "B2"
    difficulty_score: Optional[int] = None
    category: Optional[str] = "Daily Life"

class SentenceCreate(SentenceBase):
    pass

class Sentence(SentenceBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
