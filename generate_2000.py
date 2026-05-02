#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate complete seed_all_sentences.py with exactly 2000 sentences
Run: python generate_2000.py
"""

import os

output_file = r"D:\CODEcopilot\KeyGermany.de\seed_all_sentences.py"

# Build the complete Python file content
lines = []
lines.append("from app.core.database import SessionLocal, engine, Base")
lines.append("from app.models import Sentence")
lines.append("import random")
lines.append("")
lines.append("Base.metadata.create_all(bind=engine)")
lines.append("")
lines.append("# Check existing sentence count")
lines.append("session = SessionLocal()")
lines.append("try:")
lines.append("    existing_count = session.query(Sentence).count()")
lines.append("    if existing_count > 50:")
lines.append(f"        print(f'Database already has {{existing_count}} sentences (>50), skipping seed.')")
lines.append("        session.close()")
lines.append("        exit()")
lines.append("finally:")
lines.append("    session.close()")
lines.append("")
lines.append("# All 2000 sentences")
lines.append("sentences = [")
lines.append("# ==================== A1 (300 sentences) ====================")
lines.append("")

# A1: 300 sentences (10 categories x 30)
a1_data = []

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
a1_data.extend(greetings_a1)

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
a1_data.extend(personal_a1)

# Family A1 (30)
family_a1 = [
    ("Ich habe eine große Familie.", "I have a large family.", "لدي عائلة كبيرة.", 1, "Family"),
    ("Mein Vater ist 50 Jahre alt.", "My father is 50 years old.", "أبي عمره 50 عامًا.", 1, "Family"),
    ("Meine Mutter arbeitet als Krankenschwester.", "My mother works as a nurse.", "أمي تعمل كممرضة.", 2, "Family"),
    ("Wir wohnen in einem Haus mit Garten.", "We live in a house with a garden.", "نحن نعيش في منزل به حديقة.", 2, "Family"),
    ("Mein Opa ist schon in Rente.", "My grandpa is already retired.", "جدي متقاعد بالفعل.", 2, "Family"),
    ("Meine Oma kocht gerne.", "My grandma likes to cook.", "جدتي تحب الطبخ.", 1, "Family"),
    ("Ich besuche meine Familie jedes Wochenende.", "I visit my family every weekend.", "أزور عائلتي كل عطلة نهاية أسبوع.", 2, "Family"),
    ("Wir feiern Weihnachten zusammen.", "We celebrate Christmas together.", "نحتفل بعيد الميلاد معًا.", 2, "Family"),
    ("Mein Cousin studiert in Berlin.", "My cousin studies in Berlin.", "ابن عمي يدرس في برلين.", 2, "Family"),
    ("Meine Tante kommt aus Italien.", "My aunt comes from Italy.", "عمةي تأتي من إيطاليا.", 2, "Family"),
    ("Ich habe viele Verwandte in Deutschland.", "I have many relatives in Germany.", "لدي الكثير من الأقارب في ألمانيا.", 2, "Family"),
    ("Meine Eltern sind verheiratet.", "My parents are married.", "والداي متزوجان.", 1, "Family"),
    ("Mein Bruder ist jünger als ich.", "My brother is younger than me.", "أخي أصغر مني.", 2, "Family"),
    ("Meine Schwester ist älter als mich.", "My sister is older than me.", "أختي أكبر مني.", 2, "Family"),
    ("Wir essen oft zusammen zu Abend.", "We often eat dinner together.", "نحن نتناول العشاء معًا في كثير من الأحيان.", 2, "Family"),
    ("Meine Familie unterstützt mich beim Studium.", "My family supports me in my studies.", "عائلتي تدعمني في دراستي.", 3, "Family"),
    ("Ich liebe meine Familie sehr.", "I love my family very much.", "أنا أحب عائلتي كثيرًا.", 1, "Family"),
    ("Mein Onkel hat eine Firma.", "My uncle has a company.", "عمي لديه شركة.", 2, "Family"),
    ("Meine Tante arbeitet in einem Krankenhaus.", "My aunt works in a hospital.", "عمةي تعمل في مستشفى.", 2, "Family"),
    ("Ich habe eine Nichte.", "I have a niece.", "لدي ابنة أخ.", 1, "Family"),
    ("Mein Neffe ist 3 Jahre alt.", "My nephew is 3 years old.", "ابن أخي عمره 3 سنوات.", 1, "Family"),
    ("Wir fahren im Urlaub an die See.", "We go to the seaside on vacation.", "نحن نذهب إلى شاطئ البحر في العطلة.", 2, "Family"),
    ("Meine Familie kommt aus verschiedenen Ländern.", "My family comes from different countries.", "عائلتي تأتي من بلدان مختلفة.", 3, "Family"),
    ("Ich habe keine Geschwister.", "I have no siblings.", "ليس لدي إخوة.", 1, "Family"),
    ("Meine Oma ist 70 Jahre alt.", "My grandma is 70 years old.", "جدتي عمرها 70 عامًا.", 1, "Family"),
    ("Mein Opa spielt gerne Schach.", "My grandpa likes to play chess.", "جدي يحب لعب الشطرنج.", 2, "Family"),
    ("Wir haben ein Haustier, eine Katze.", "We have a pet, a cat.", "لدينا حيوان أليف، قطة.", 2, "Family"),
    ("Meine Schwester lernt auch Deutsch.", "My sister also learns German.", "أختي تتعلم الألمانية أيضًا.", 2, "Family"),
    ("Mein Vater ist Ingenieur.", "My father is an engineer.", "أبي مهندس.", 2, "Family"),
    ("Meine Mutter kocht jeden Tag.", "My mother cooks every day.", "أمي تطبخ كل يوم.", 1, "Family"),
]
a1_data.extend(family_a1)

# Food & Drinks A1 (30)
food_a1 = [
    ("Ich trinke gerne Kaffee am Morgen.", "I like to drink coffee in the morning.", "أنا أحب شرب القهوة في الصباح.", 1, "Food & Drinks"),
    ("Ich esse gerne Pizza.", "I like to eat pizza.", "أنا أحب أكل البيتزا.", 1, "Food & Drinks"),
    ("Wasser ist gesund.", "Water is healthy.", "الماء صحي.", 1, "Food & Drinks"),
    ("Ich koche oft zu Hause.", "I often cook at home.", "أنا أطبخ في المنزل في كثير من الأحيان.", 2, "Food & Drinks"),
    ("Das Brot schmeckt gut.", "The bread tastes good.", "الخبز طعمه جيد.", 1, "Food & Drinks"),
    ("Ich trinke Tee am Abend.", "I drink tea in the evening.", "أنا أشرب الشاي في المساء.", 1, "Food & Drinks"),
    ("Obst ist gut für die Gesundheit.", "Fruit is good for health.", "الفاكهة جيدة للصحة.", 2, "Food & Drinks"),
    ("Ich esse ein Sandwich zum Frühstück.", "I eat a sandwich for breakfast.", "أنا أتناول شطيرة للإفطار.", 2, "Food & Drinks"),
    ("Saft ist lecker.", "Juice is delicious.", "العصير لذيذ.", 1, "Food & Drinks"),
    ("Ich gehe oft ins Restaurant.", "I often go to the restaurant.", "أنا أذهب إلى المطعم في كثير من الأحيان.", 2, "Food & Drinks"),
    ("Die Suppe ist heiß.", "The soup is hot.", "الحساء ساخن.", 1, "Food & Drinks"),
    ("Ich mag Schokolade.", "I like chocolate.", "أنا أحب الشوكولاتة.", 1, "Food & Drinks"),
    ("Milch ist gut für Kinder.", "Milk is good for children.", "الحليب جيد للأطفال.", 2, "Food & Drinks"),
    ("Ich kaufe Lebensmittel im Supermarkt.", "I buy groceries at the supermarket.", "أنا أشتري البقالة في السوبر ماركت.", 2, "Food & Drinks"),
    ("Das Eis schmilzt schnell.", "The ice cream melts quickly.", "الآيس كريم يذوب بسرعة.", 2, "Food & Drinks"),
    ("Ich trinke kein Alkohol.", "I don't drink alcohol.", "أنا لا أشرب الكحول.", 1, "Food & Drinks"),
    ("Gemüse ist wichtig für die Ernährung.", "Vegetables are important for nutrition.", "الخضروات مهمة للتغذية.", 3, "Food & Drinks"),
    ("Ich esse gerne Nudeln.", "I like to eat pasta.", "أنا أحب أكل المعكرونة.", 1, "Food & Drinks"),
    ("Der Kaffee ist zu stark.", "The coffee is too strong.", "القهوة قوية جدًا.", 2, "Food & Drinks"),
    ("Ich koche für meine Familie.", "I cook for my family.", "أنا أطبخ لعائلتي.", 2, "Food & Drinks"),
    ("Das Bier ist kalt.", "The beer is cold.", "البيرة باردة.", 1, "Food & Drinks"),
    ("Ich trinke Wasser ohne Kohlensäure.", "I drink water without carbonation.", "أنا أشرب الماء بدون غاز.", 2, "Food & Drinks"),
    ("Die Zitrone ist sauer.", "The lemon is sour.", "الليمون حامض.", 1, "Food & Drinks"),
    ("Ich esse einen Apfel jeden Tag.", "I eat an apple every day.", "أنا أتناول تفاحة كل يوم.", 2, "Food & Drinks"),
    ("Das Restaurant hat gute Bewertungen.", "The restaurant has good reviews.", "المطعم له تقييمات جيدة.", 3, "Food & Drinks"),
    ("Ich mag italienisches Essen.", "I like Italian food.", "أنا أحب الطعام الإيطالي.", 2, "Food & Drinks"),
    ("Der Kuchen schmeckt herrlich.", "The cake tastes wonderful.", "الكعكة طعمها رائع.", 2, "Food & Drinks"),
    ("Ich trinke Orangensaft zum Frühstück.", "I drink orange juice for breakfast.", "أنا أشرب عصير البرتقال للإفطار.", 2, "Food & Drinks"),
    ("Frisches Brot ist am besten.", "Fresh bread is the best.", "الخبز الطازج هو الأفضل.", 2, "Food & Drinks"),
    ("Ich trinke gerne Saft.", "I like to drink juice.", "أنا أحب شرب العصير.", 1, "Food & Drinks"),
]
a1_data.extend(food_a1)

# Shopping A1 (30)
shopping_a1 = [
    ("Ich gehe einkaufen.", "I go shopping.", "أنا أذهب للتسوق.", 1, "Shopping"),
    ("Das Hemd kostet 20 Euro.", "The shirt costs 20 euros.", "القميص يكلف 20 يورو.", 2, "Shopping"),
    ("Ich brauche neue Schuhe.", "I need new shoes.", "أحتاج إلى أحذية جديدة.", 1, "Shopping"),
    ("Das ist zu teuer.", "That is too expensive.", "هذا باهظ الثمن.", 1, "Shopping"),
    ("Ich kaufe ein Geschenk für meine Mutter.", "I buy a gift for my mother.", "أنا أشتري هدية لأمي.", 2, "Shopping"),
    ("Die Jacke passt mir gut.", "The jacket fits me well.", "السترة تناسبني جيدًا.", 2, "Shopping"),
    ("Ich bezahle mit Karte.", "I pay with card.", "أنا أدفع بالبطاقة.", 2, "Shopping"),
    ("Der Supermarkt ist um die Ecke.", "The supermarket is around the corner.", "السوبر ماركت خلف الزاوية.", 2, "Shopping"),
    ("Ich suche eine Hose.", "I am looking for pants.", "أنا أبحث عن بنطال.", 1, "Shopping"),
    ("Das Angebot ist gut.", "The offer is good.", "العرض جيد.", 1, "Shopping"),
    ("Ich kaufe Obst und Gemüse.", "I buy fruit and vegetables.", "أنا أشتري الفواكه والخضروات.", 2, "Shopping"),
    ("Die Jeans sind im Angebot.", "The jeans are on sale.", "الجينز معروض للبيع.", 2, "Shopping"),
    ("Ich habe die Quittung verloren.", "I lost the receipt.", "لقد فقدت الإيصال.", 2, "Shopping"),
    ("Kann ich das umtauschen?", "Can I exchange this?", "هل يمكنني استبدال هذا؟", 2, "Shopping"),
    ("Das Geschäft öffnet um 9 Uhr.", "The store opens at 9 o'clock.", "المتجر يفتح في الساعة 9.", 2, "Shopping"),
    ("Ich brauche einen neuen Rucksack.", "I need a new backpack.", "أحتاج إلى حقيبة ظهر جديدة.", 2, "Shopping"),
    ("Die Schuhe sind bequem.", "The shoes are comfortable.", "الأحذية مريحة.", 2, "Shopping"),
    ("Ich kaufe ein Buch.", "I buy a book.", "أنا أشتري كتابًا.", 1, "Shopping"),
    ("Das ist ein guter Preis.", "That is a good price.", "هذا سعر جيد.", 1, "Shopping"),
    ("Ich gehe in die Mall.", "I go to the mall.", "أنا أذهب إلى المركز التجاري.", 1, "Shopping"),
    ("Die Tasche ist schön.", "The bag is beautiful.", "الحقيبة جميلة.", 1, "Shopping"),
    ("Ich habe nicht genug Geld.", "I don't have enough money.", "ليس لدي ما يكفي من المال.", 2, "Shopping"),
    ("Kann ich mit Kreditkarte zahlen?", "Can I pay with credit card?", "هل يمكنني الدفع ببطاقة الإئتمان؟", 3, "Shopping"),
    ("Das Geschäft ist geschlossen.", "The store is closed.", "المتجر مغلق.", 1, "Shopping"),
    ("Ich kaufe Geschenke für Weihnachten.", "I buy Christmas gifts.", "أنا أشتري هدايا عيد الميلاد.", 2, "Shopping"),
    ("Die Bluse passt nicht.", "The blouse does not fit.", "البلوزة لا تناسب.", 2, "Shopping"),
    ("Ich suche ein Geschenk für meinen Bruder.", "I am looking for a gift for my brother.", "أنا أبحث عن هدية لأخي.", 2, "Shopping"),
    ("Das ist reduziert.", "That is reduced.", "هذا مخفض.", 1, "Shopping"),
    ("Ich kaufe Milch und Eier.", "I buy milk and eggs.", "أنا أشتري الحليب والبيض.", 2, "Shopping"),
    ("Der Verkäufer ist freundlich.", "The salesperson is friendly.", "مندوب المبيعات ودود.", 2, "Shopping"),
]
a1_data.extend(shopping_a1)

# Directions A1 (30)
directions_a1 = [
    ("Wo ist der Bahnhof?", "Where is the train station?", "أين محطة القطار؟", 1, "Directions"),
    ("Gehen Sie geradeaus.", "Go straight ahead.", "اذهب مباشرة.", 1, "Directions"),
    ("Biegen Sie links ab.", "Turn left.", "انعطف يسارًا.", 1, "Directions"),
    ("Biegen Sie rechts ab.", "Turn right.", "انعطف يمينًا.", 1, "Directions"),
    ("Die Bank ist neben dem Supermarkt.", "The bank is next to the supermarket.", "البنك بجوار السوبر ماركت.", 2, "Directions"),
    ("Wie komme ich zum Flughafen?", "How do I get to the airport?", "كيف أصل إلى المطار؟", 2, "Directions"),
    ("Die Post ist gegenüber der Schule.", "The post office is opposite the school.", "مكتب البريد مقابل المدرسة.", 2, "Directions"),
    ("Gehen Sie über die Brücke.", "Go over the bridge.", "اذهب فوق الجسر.", 2, "Directions"),
    ("Die Straße heißt Hauptstraße.", "The street is called Main Street.", "الشارع يسمى الشارع الرئيسي.", 2, "Directions"),
    ("Wo ist die Toilette?", "Where is the toilet?", "أين المرحاض؟", 1, "Directions"),
    ("Die Apotheke ist um die Ecke.", "The pharmacy is around the corner.", "الصيدلية خلف الزاوية.", 2, "Directions"),
    ("Fahren Sie bis zur Ampel.", "Drive until the traffic light.", "اقود حتى إشارة المرور.", 2, "Directions"),
    ("Die Bibliothek ist hinter dem Rathaus.", "The library is behind the town hall.", "المكتبة خلف قاعة المدينة.", 3, "Directions"),
    ("Wo ist die nächste U-Bahn-Station?", "Where is the nearest subway station?", "أين أقرب محطة مترو؟", 3, "Directions"),
    ("Gehen Sie die Treppe hoch.", "Go up the stairs.", "اصعد الدرج.", 2, "Directions"),
    ("Die Haltestelle ist dort drüben.", "The stop is over there.", "الموقف هناك.", 2, "Directions"),
    ("Ich habe mich verlaufen.", "I got lost.", "لقد ضللت طريقي.", 2, "Directions"),
    ("Können Sie mir den Weg zeigen?", "Can you show me the way?", "هل يمكنك إرشادي إلى الطريق؟", 2, "Directions"),
    ("Die Kirche ist im Zentrum.", "The church is in the center.", "الكنيسة في المركز.", 2, "Directions"),
    ("Wo ist der Parkplatz?", "Where is the parking lot?", "أين موقف السيارات؟", 1, "Directions"),
    ("Fahren Sie nicht zu schnell.", "Don't drive too fast.", "لا تقود بسرعة كبيرة.", 2, "Directions"),
    ("Die Schule ist gegenüber dem Park.", "The school is opposite the park.", "المدرسة مقابل الحديقة.", 2, "Directions"),
    ("Gehen Sie durch den Park.", "Go through the park.", "اذهب عبر الحديقة.", 2, "Directions"),
    ("Die Adresse ist falsch.", "The address is wrong.", "العنوان خاطئ.", 2, "Directions"),
    ("Wo ist das Hotel?", "Where is the hotel?", "أين الفندق؟", 1, "Directions"),
    ("Die Bushaltestelle ist vor dem Haus.", "The bus stop is in front of the house.", "موقف الحافلة أمام المنزل.", 2, "Directions"),
    ("Ich brauche eine Karte.", "I need a map.", "أحتاج إلى خريطة.", 1, "Directions"),
    ("Die Stadtmauer ist alt.", "The city wall is old.", "سور المدينة قديم.", 2, "Directions"),
    ("Gehen Sie am Fluss entlang.", "Walk along the river.", "امشي على طول النهر.", 2, "Directions"),
    ("Die Polizeistation ist in der Nähe.", "The police station is nearby.", "مركز الشرطة قريب.", 2, "Directions"),
]
a1_data.extend(directions_a1)

print(f"A1 data collected: {len(a1_data)} sentences")
print("Need to add more A1 categories (Transport, Travel, Time & Date, Weather)...")

# Due to length, let's write what we have and continue in parts
# Write the file with what we have, then append more
