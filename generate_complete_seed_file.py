#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate complete seed_all_sentences.py with 2000 sentences
Run: python generate_complete_seed_file.py
"""

import os

# All sentences will be collected here
sentences_data = []

# ==================== A1 (300 sentences) ====================
# Greetings A1 (30)
greetings_a1 = [
    ("Hallo!", "Hello!", "مرحبًا!", 1, "Greetings"),
    ("Guten Morgen!", "Good morning!", "صباح الخير!", 1, "Greetings"),
    ("Guten Tag!", "Good day!", "مرحبًا بك!", 1, "Greetings"),
    ("Guten Abend!", "Good evening!", "مساء الخير!", 1, "Greetings"),
    ("Auf Wiedersehen!", "Goodbye!", "وداعًا!", 1, "Greetings"),
    ("Tschüss!", "Bye!", "مع السلامة!", 1, "Greetings"),
    ("Bis bald!", "See you soon!", "أراك قريبًا!", 1, "Greetings"),
    ("Bis morgen!", "See you tomorrow!", "أراك غدًا!", 1, "Greetings"),
    ("Wie geht es dir?", "How are you?", "كيف حالك؟", 1, "Greetings"),
    ("Mir geht es gut, danke.", "I'm fine, thank you.", "أنا بخير، شكرًا.", 1, "Greetings"),
    ("Wie heißt du?", "What's your name?", "ما اسمك؟", 1, "Greetings"),
    ("Ich heiße Max.", "My name is Max.", "اسمي ماكس.", 1, "Greetings"),
    ("Woher kommst du?", "Where are you from?", "من أين تأتي؟", 1, "Greetings"),
    ("Ich komme aus Deutschland.", "I come from Germany.", "أنا أتيت من ألمانيا.", 1, "Greetings"),
    ("Wie alt bist du?", "How old are you?", "كم عمرك؟", 1, "Greetings"),
    ("Ich bin 20 Jahre alt.", "I am 20 years old.", "أنا عمري 20 عامًا.", 1, "Greetings"),
    ("Was machst du hier?", "What are you doing here?", "ماذا تفعل هنا؟", 1, "Greetings"),
    ("Ich lerne Deutsch.", "I'm learning German.", "أنا أتعلم الألمانية.", 1, "Greetings"),
    ("Sprechen Sie Englisch?", "Do you speak English?", "هل تتحدث الإنجليزية؟", 2, "Greetings"),
    ("Ja, ein bisschen.", "Yes, a little.", "نعم، قليلًا.", 1, "Greetings"),
    ("Ich verstehe nicht.", "I don't understand.", "أنا لا أفهم.", 1, "Greetings"),
    ("Können Sie das bitte wiederholen?", "Can you repeat that please?", "هل يمكنك تكرار ذلك من فضلك؟", 2, "Greetings"),
    ("Entschuldigung!", "Excuse me!", "عذرًا!", 1, "Greetings"),
    ("Danke schön!", "Thank you very much!", "شكرًا جزيلًا!", 1, "Greetings"),
    ("Bitte schön!", "You're welcome!", "عفوًا!", 1, "Greetings"),
    ("Keine Ursache.", "No problem.", "لا مشكلة.", 1, "Greetings"),
    ("Viel Glück!", "Good luck!", "حظًا سعيدًا!", 1, "Greetings"),
    ("Alles Gute!", "All the best!", "كل التوفيق!", 1, "Greetings"),
    ("Herzlichen Glückwunsch!", "Congratulations!", "مبروك!", 2, "Greetings"),
    ("Frohe Weihnachten!", "Merry Christmas!", "عيد ميلاد مجيد!", 2, "Greetings"),
]

# Personal Info A1 (30)
personal_a1 = [
    ("Ich heiße Anna.", "My name is Anna.", "اسمي آنا.", 1, "Personal Info"),
    ("Ich bin 25 Jahre alt.", "I am 25 years old.", "أنا عمري 25 عامًا.", 1, "Personal Info"),
    ("Ich wohne in Berlin.", "I live in Berlin.", "أنا أعيش في برلين.", 1, "Personal Info"),
    ("Ich komme aus München.", "I come from Munich.", "أنا أتيت من ميونخ.", 1, "Personal Info"),
    ("Meine Adresse ist Hauptstraße 10.", "My address is Main Street 10.", "عنواني هو الشارع الرئيسي 10.", 2, "Personal Info"),
    ("Meine Telefonnummer ist 0123 456789.", "My phone number is 0123 456789.", "رقم هاتفي هو 0123 456789.", 2, "Personal Info"),
    ("Ich bin ledig.", "I am single.", "أنا أعزب.", 1, "Personal Info"),
    ("Ich habe keine Kinder.", "I have no children.", "ليس لدي أطفال.", 1, "Personal Info"),
    ("Ich spreche Deutsch und Englisch.", "I speak German and English.", "أنا أتحدث الألمانية والإنجليزية.", 2, "Personal Info"),
    ("Ich lerne Spanisch.", "I am learning Spanish.", "أنا أتعلم الإسبانية.", 2, "Personal Info"),
    ("Ich arbeite als Verkäufer.", "I work as a salesperson.", "أنا أعمل كمندوب مبيعات.", 2, "Personal Info"),
    ("Ich studiere Medizin.", "I study medicine.", "أنا أدرس الطب.", 2, "Personal Info"),
    ("Mein Geburtsdatum ist der 5. Mai 2000.", "My date of birth is May 5, 2000.", "تاريخ ميلادي هو 5 مايو 2000.", 3, "Personal Info"),
    ("Ich bin deutscher Staatsbürger.", "I am a German citizen.", "أنا مواطن ألماني.", 2, "Personal Info"),
    ("Ich habe einen deutschen Pass.", "I have a German passport.", "لدي جواز سفر ألماني.", 2, "Personal Info"),
    ("Ich fahre nach Hause.", "I drive home.", "أنا أقود إلى المنزل.", 1, "Personal Info"),
    ("Ich gehe zur Schule.", "I go to school.", "أنا أذهب إلى المدرسة.", 1, "Personal Info"),
    ("Ich habe Deutschkurs.", "I have German class.", "لدي فصل ألماني.", 2, "Personal Info"),
    ("Meine Muttersprache ist Arabisch.", "My native language is Arabic.", "لغتي الأم هي العربية.", 2, "Personal Info"),
    ("Ich lerne Deutsch seit einem Jahr.", "I have been learning German for a year.", "أنا أتعلم الألمانية منذ عام.", 3, "Personal Info"),
    ("Ich wohne in einer Wohnung.", "I live in an apartment.", "أنا أعيش في شقة.", 2, "Personal Info"),
    ("Meine Wohnung hat drei Zimmer.", "My apartment has three rooms.", "شقتي بها ثلاث غرف.", 2, "Personal Info"),
    ("Ich habe ein Auto.", "I have a car.", "لدي سيارة.", 1, "Personal Info"),
    ("Ich fahre jeden Tag zur Arbeit.", "I drive to work every day.", "أنا أقود إلى العمل كل يوم.", 2, "Personal Info"),
    ("Ich komme aus der Schweiz.", "I come from Switzerland.", "أنا أتيت من سويسرا.", 1, "Personal Info"),
    ("Ich bin Schweizer.", "I am Swiss.", "أنا سويسري.", 1, "Personal Info"),
    ("Ich arbeite in einer Bank.", "I work in a bank.", "أنا أعمل في بنك.", 2, "Personal Info"),
    ("Ich bin Student.", "I am a student.", "أنا طالب.", 1, "Personal Info"),
    ("Ich studiere Jura.", "I study law.", "أنا أدرس القانون.", 2, "Personal Info"),
    ("Ich habe eine Schwester.", "I have a sister.", "لدي أخت.", 1, "Personal Info"),
]

for s in greetings_a1 + personal_a1:
    sentences_data.append(s)

print(f"Added A1 sentences. Total so far: {len(sentences_data)}")
print("Script created. Now add more sentence groups...")
