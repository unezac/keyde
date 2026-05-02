#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script to create complete seed_all_sentences.py with 2000 sentences
A1: 300 sentences (difficulty 1-3)
A2: 400 sentences (difficulty 2-4)
B1: 500 sentences (difficulty 3-5)
B2: 400 sentences (difficulty 4-7)
C1: 400 sentences (difficulty 6-9)
"""

import os

output_path = r"D:\CODEcopilot\KeyGermany.de\seed_all_sentences.py"

# Start building the file content
content = """from app.core.database import SessionLocal, engine, Base
from app.models import Sentence
import random

Base.metadata.create_all(bind=engine)

# Check existing sentence count
session = SessionLocal()
try:
    existing_count = session.query(Sentence).count()
    if existing_count > 50:
        print(f"Database already has {existing_count} sentences (>50), skipping seed.")
        session.close()
        exit()
finally:
    session.close()

# All 2000 sentences
sentences = [
"""

# A1 sentences (300) - 10 categories x 30 each
a1_sentences = [
    # Greetings A1 (30)
    {"german_text": "Hallo!", "english_translation": "Hello!", "arabic_translation": "مرحبًا!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Guten Morgen!", "english_translation": "Good morning!", "arabic_translation": "صباح الخير!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Guten Tag!", "english_translation": "Good day!", "arabic_translation": "مرحبًا بك!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Guten Abend!", "english_translation": "Good evening!", "arabic_translation": "مساء الخير!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Auf Wiedersehen!", "english_translation": "Goodbye!", "arabic_translation": "وداعًا!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Tschüss!", "english_translation": "Bye!", "arabic_translation": "مع السلامة!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Bis bald!", "english_translation": "See you soon!", "arabic_translation": "أراك قريبًا!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Bis morgen!", "english_translation": "See you tomorrow!", "arabic_translation": "أراك غدًا!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Wie geht es dir?", "english_translation": "How are you?", "arabic_translation": "كيف حالك؟", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Mir geht es gut, danke.", "english_translation": "I'm fine, thank you.", "arabic_translation": "أنا بخير، شكرًا.", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Wie heißt du?", "english_translation": "What's your name?", "arabic_translation": "ما اسمك؟", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Ich heiße Max.", "english_translation": "My name is Max.", "arabic_translation": "اسمي ماكس.", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Woher kommst du?", "english_translation": "Where are you from?", "arabic_translation": "من أين تأتي؟", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Ich komme aus Deutschland.", "english_translation": "I come from Germany.", "arabic_translation": "أنا أتيت من ألمانيا.", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Wie alt bist du?", "english_translation": "How old are you?", "arabic_translation": "كم عمرك؟", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Ich bin 20 Jahre alt.", "english_translation": "I am 20 years old.", "arabic_translation": "أنا عمري 20 عامًا.", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Was machst du hier?", "english_translation": "What are you doing here?", "arabic_translation": "ماذا تفعل هنا؟", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Ich lerne Deutsch.", "english_translation": "I'm learning German.", "arabic_translation": "أنا أتعلم الألمانية.", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Sprechen Sie Englisch?", "english_translation": "Do you speak English?", "arabic_translation": "هل تتحدث الإنجليزية؟", "level": "A1", "difficulty_score": 2, "category": "Greetings"},
    {"german_text": "Ja, ein bisschen.", "english_translation": "Yes, a little.", "arabic_translation": "نعم، قليلًا.", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Ich verstehe nicht.", "english_translation": "I don't understand.", "arabic_translation": "أنا لا أفهم.", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Konnen Sie das bitte wiederholen?", "english_translation": "Can you repeat that please?", "arabic_translation": "هل يمكنك تكرار ذلك من فضلك؟", "level": "A1", "difficulty_score": 2, "category": "Greetings"},
    {"german_text": "Entschuldigung!", "english_translation": "Excuse me!", "arabic_translation": "عذرًا!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Danke schon!", "english_translation": "Thank you very much!", "arabic_translation": "شكرًا جزيلًا!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Bitte schon!", "english_translation": "You're welcome!", "arabic_translation": "عفوًا!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Keine Ursache.", "english_translation": "No problem.", "arabic_translation": "لا مشكلة.", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Viel Gluck!", "english_translation": "Good luck!", "arabic_translation": "حظًا سعيدًا!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Alles Gute!", "english_translation": "All the best!", "arabic_translation": "كل التوفيق!", "level": "A1", "difficulty_score": 1, "category": "Greetings"},
    {"german_text": "Herzlichen Gluckwunsch!", "english_translation": "Congratulations!", "arabic_translation": "مبروك!", "level": "A1", "difficulty_score": 2, "category": "Greetings"},
    {"german_text": "Frohe Weihnachten!", "english_translation": "Merry Christmas!", "arabic_translation": "عيد ميلاد مجيد!", "level": "A1", "difficulty_score": 2, "category": "Greetings"},
]

print("Generator created. Need to add more sentences...")
print("Run this script to generate the complete seed file.")
