from sqlalchemy import Column, Integer, String, Text, DateTime, func

try:
    from ..core.database import Base
except ImportError:
    from core.database import Base

class Sentence(Base):
    __tablename__ = "sentences"

    id = Column(Integer, primary_key=True, index=True)
    german_text = Column(Text, nullable=False)
    english_translation = Column(Text, nullable=False)
    arabic_translation = Column(Text, nullable=False)
    level = Column(String(5), default="B2")
    difficulty_score = Column(Integer)
    category = Column(String(50), default="Daily Life", index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
