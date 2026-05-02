import json

# This script generates seed_all_sentences.py

# Header
header = """from app.core.database import SessionLocal, engine, Base
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

# A1 sentences (300) - difficulty 1-3
a1_sentences = []

# Greetings A1 (30)
greetings_a1 = [
    ("Hallo!", "Hello!", "مرحبًا!", 1),
    ("Guten Morgen!", "Good morning!", "صباح الخير!", 1),
    ("Guten Tag!", "Good day!", "مرحبًا بك!", 1),
    ("Guten Abend!", "Good evening!", "مساء الخير!", 1),
    ("Auf Wiedersehen!", "Goodbye!", "وداعًا!", 1),
    ("Tschüss!", "Bye!", "مع السلامة!", 1),
    ("Bis bald!", "See you soon!", "أراك قريبًا!", 1),
    ("Bis morgen!", "See you tomorrow!", "أراك غدًا!", 1),
    ("Wie geht es dir?", "How are you?", "كيف حالك؟", 1),
    ("Mir geht es gut, danke.", "I'm fine, thank you.", "أنا بخير، شكرًا.", 1),
    ("Wie heißt du?", "What's your name?", "ما اسمك؟", 1),
    ("Ich heiße Max.", "My name is Max.", "اسمي ماكس.", 1),
    ("Woher kommst du?", "Where are you from?", "من أين تأتي؟", 1),
    ("Ich komme aus Deutschland.", "I come from Germany.", "أنا أتيت من ألمانيا.", 1),
    ("Wie alt bist du?", "How old are you?", "كم عمرك؟", 1),
    ("Ich bin 20 Jahre alt.", "I am 20 years old.", "أنا عمري 20 عامًا.", 1),
    ("Was machst du hier?", "What are you doing here?", "ماذا تفعل هنا؟", 1),
    ("Ich lerne Deutsch.", "I'm learning German.", "أنا أتعلم الألمانية.", 1),
    ("Sprechen Sie Englisch?", "Do you speak English?", "هل تتحدث الإنجليزية؟", 2),
    ("Ja, ein bisschen.", "Yes, a little.", "نعم، قليلًا.", 1),
    ("Ich verstehe nicht.", "I don't understand.", "أنا لا أفهم.", 1),
    ("Können Sie das bitte wiederholen?", "Can you repeat that please?", "هل يمكنك تكرار ذلك من فضلك؟", 2),
    ("Entschuldigung!", "Excuse me!", "عذرًا!", 1),
    ("Danke schön!", "Thank you very much!", "شكرًا جزيلًا!", 1),
    ("Bitte schön!", "You're welcome!", "عفوًا!", 1),
    ("Keine Ursache.", "No problem.", "لا مشكلة.", 1),
    ("Viel Glück!", "Good luck!", "حظًا سعيدًا!", 1),
    ("Alles Gute!", "All the best!", "كل التوفيق!", 1),
    ("Herzlichen Glückwunsch!", "Congratulations!", "مبروك!", 2),
    ("Frohe Weihnachten!", "Merry Christmas!", "عيد ميلاد مجيد!", 2),
]

for g in greetings_a1:
    a1_sentences.append(f'    {{"german_text": "{g[0]}", "english_translation": "{g[1]}", "arabic_translation": "{g[2]}", "level": "A1", "difficulty_score": {g[3]}, "category": "Greetings"}},')

# Personal Info A1 (30)
personal_a1 = [
    ("Ich heiße Anna.", "My name is Anna.", "اسمي آنا.", 1),
    ("Ich bin 25 Jahre alt.", "I am 25 years old.", "أنا عمري 25 عامًا.", 1),
    ("Ich wohne in Berlin.", "I live in Berlin.", "أنا أعيش في برلين.", 1),
    ("Ich komme aus München.", "I come from Munich.", "أنا أتيت من ميونخ.", 1),
    ("Meine Adresse ist Hauptstraße 10.", "My address is Main Street 10.", "عنواني هو الشارع الرئيسي 10.", 2),
    ("Meine Telefonnummer ist 0123 456789.", "My phone number is 0123 456789.", "رقم هاتفي هو 0123 456789.", 2),
    ("Ich bin ledig.", "I am single.", "أنا أعزب.", 1),
    ("Ich habe keine Kinder.", "I have no children.", "ليس لدي أطفال.", 1),
    ("Ich spreche Deutsch und Englisch.", "I speak German and English.", "أنا أتحدث الألمانية والإنجليزية.", 2),
    ("Ich lerne Spanisch.", "I am learning Spanish.", "أنا أتعلم الإسبانية.", 2),
    ("Ich arbeite als Verkäufer.", "I work as a salesperson.", "أنا أعمل كمندوب مبيعات.", 2),
    ("Ich studiere Medizin.", "I study medicine.", "أنا أدرس الطب.", 2),
    ("Mein Geburtsdatum ist der 5. Mai 2000.", "My date of birth is May 5, 2000.", "تاريخ ميلادي هو 5 مايو 2000.", 3),
    ("Ich bin deutscher Staatsbürger.", "I am a German citizen.", "أنا مواطن ألماني.", 2),
    ("Ich habe einen deutschen Pass.", "I have a German passport.", "لدي جواز سفر ألماني.", 2),
    ("Ich fahre nach Hause.", "I drive home.", "أنا أقود إلى المنزل.", 1),
    ("Ich gehe zur Schule.", "I go to school.", "أنا أذهب إلى المدرسة.", 1),
    ("Ich habe Deutschkurs.", "I have German class.", "لدي فصل ألماني.", 2),
    ("Meine Muttersprache ist Arabisch.", "My native language is Arabic.", "لغتي الأم هي العربية.", 2),
    ("Ich lerne Deutsch seit einem Jahr.", "I have been learning German for a year.", "أنا أتعلم الألمانية منذ عام.", 3),
    ("Ich wohne in einer Wohnung.", "I live in an apartment.", "أنا أعيش في شقة.", 2),
    ("Meine Wohnung hat drei Zimmer.", "My apartment has three rooms.", "شقتي بها ثلاث غرف.", 2),
    ("Ich habe ein Auto.", "I have a car.", "لدي سيارة.", 1),
    ("Ich fahre jeden Tag zur Arbeit.", "I drive to work every day.", "أنا أقود إلى العمل كل يوم.", 2),
    ("Ich komme aus der Schweiz.", "I come from Switzerland.", "أنا أتيت من سويسرا.", 1),
    ("Ich bin Schweizer.", "I am Swiss.", "أنا سويسري.", 1),
    ("Ich arbeite in einer Bank.", "I work in a bank.", "أنا أعمل في بنك.", 2),
    ("Ich bin Student.", "I am a student.", "أنا طالب.", 1),
    ("Ich studiere Jura.", "I study law.", "أنا أدرس القانون.", 2),
    ("Ich habe eine Schwester.", "I have a sister.", "لدي أخت.", 1),
    ("Ich habe einen Bruder.", "I have a brother.", "لدي أخ.", 1),
]

for p in personal_a1:
    a1_sentences.append(f'    {{"german_text": "{p[0]}", "english_translation": "{p[1]}", "arabic_translation": "{p[2]}", "level": "A1", "difficulty_score": {p[3]}, "category": "Personal Info"}},')

# Family A1 (30)
family_a1 = [
    ("Ich habe eine große Familie.", "I have a large family.", "لدي عائلة كبيرة.", 1),
    ("Mein Vater ist 50 Jahre alt.", "My father is 50 years old.", "أبي عمره 50 عامًا.", 1),
    ("Meine Mutter arbeitet als Krankenschwester.", "My mother works as a nurse.", "أمي تعمل كممرضة.", 2),
    ("Wir wohnen in einem Haus mit Garten.", "We live in a house with a garden.", "نحن نعيش في منزل به حديقة.", 2),
    ("Mein Opa ist schon in Rente.", "My grandpa is already retired.", "جدي متقاعد بالفعل.", 2),
    ("Meine Oma kocht gerne.", "My grandma likes to cook.", "جدتي تحب الطبخ.", 1),
    ("Ich besuche meine Familie jedes Wochenende.", "I visit my family every weekend.", "أزور عائلتي كل عطلة نهاية أسبوع.", 2),
    ("Wir feiern Weihnachten zusammen.", "We celebrate Christmas together.", "نحتفل بعيد الميلاد معًا.", 2),
    ("Mein Cousin studiert in Berlin.", "My cousin studies in Berlin.", "ابن عمي يدرس في برلين.", 2),
    ("Meine Tante kommt aus Italien.", "My aunt comes from Italy.", "عمةي تأتي من إيطاليا.", 2),
    ("Ich habe viele Verwandte in Deutschland.", "I have many relatives in Germany.", "لدي الكثير من الأقارب في ألمانيا.", 2),
    ("Meine Eltern sind verheiratet.", "My parents are married.", "والداي متزوجان.", 1),
    ("Mein Bruder ist jünger als ich.", "My brother is younger than me.", "أخي أصغر مني.", 2),
    ("Meine Schwester ist älter als mich.", "My sister is older than me.", "أختي أكبر مني.", 2),
    ("Wir essen oft zusammen zu Abend.", "We often eat dinner together.", "نحن نتناول العشاء معًا في كثير من الأحيان.", 2),
    ("Meine Familie unterstützt mich beim Studium.", "My family supports me in my studies.", "عائلتي تدعمني في دراستي.", 3),
    ("Ich liebe meine Familie sehr.", "I love my family very much.", "أنا أحب عائلتي كثيرًا.", 1),
    ("Mein Onkel hat eine Firma.", "My uncle has a company.", "عمي لديه شركة.", 2),
    ("Meine Tante arbeitet in einem Krankenhaus.", "My aunt works in a hospital.", "عمةي تعمل في مستشفى.", 2),
    ("Ich habe eine Nichte.", "I have a niece.", "لدي ابنة أخ.", 1),
    ("Mein Neffe ist 3 Jahre alt.", "My nephew is 3 years old.", "ابن أخي عمره 3 سنوات.", 1),
    ("Wir fahren im Urlaub an die See.", "We go to the seaside on vacation.", "نحن نذهب إلى شاطئ البحر في العطلة.", 2),
    ("Meine Familie kommt aus verschiedenen Ländern.", "My family comes from different countries.", "عائلتي تأتي من بلدان مختلفة.", 3),
    ("Ich habe keine Geschwister.", "I have no siblings.", "ليس لدي إخوة.", 1),
    ("Meine Oma ist 70 Jahre alt.", "My grandma is 70 years old.", "جدتي عمرها 70 عامًا.", 1),
    ("Mein Opa spielt gerne Schach.", "My grandpa likes to play chess.", "جدي يحب لعب الشطرنج.", 2),
    ("Wir haben ein Haustier, eine Katze.", "We have a pet, a cat.", "لدينا حيوان أليف، قطة.", 2),
    ("Meine Schwester lernt auch Deutsch.", "My sister also learns German.", "أختي تتعلم الألمانية أيضًا.", 2),
    ("Mein Vater ist Ingenieur.", "My father is an engineer.", "أبي مهندس.", 2),
    ("Meine Mutter kocht jeden Tag.", "My mother cooks every day.", "أمي تطبخ كل يوم.", 1),
    ("Ich besuche meinen Opa am Sonntag.", "I visit my grandpa on Sunday.", "أزور جدي يوم الأحد.", 2),
]

for f in family_a1:
    a1_sentences.append(f'    {{"german_text": "{f[0]}", "english_translation": "{f[1]}", "arabic_translation": "{f[2]}", "level": "A1", "difficulty_score": {f[3]}, "category": "Family"}},')

# Food & Drinks A1 (30)
food_a1 = [
    ("Ich trinke gerne Kaffee am Morgen.", "I like to drink coffee in the morning.", "أنا أحب شرب القهوة في الصباح.", 1),
    ("Ich esse gerne Pizza.", "I like to eat pizza.", "أنا أحب أكل البيتزا.", 1),
    ("Wasser ist gesund.", "Water is healthy.", "الماء صحي.", 1),
    ("Ich koche oft zu Hause.", "I often cook at home.", "أنا أطبخ في المنزل في كثير من الأحيان.", 2),
    ("Das Brot schmeckt gut.", "The bread tastes good.", "الخبز طعمه جيد.", 1),
    ("Ich trinke Tee am Abend.", "I drink tea in the evening.", "أنا أشرب الشاي في المساء.", 1),
    ("Obst ist gut für die Gesundheit.", "Fruit is good for health.", "الفاكهة جيدة للصحة.", 2),
    ("Ich esse ein Sandwich zum Frühstück.", "I eat a sandwich for breakfast.", "أنا أتناول شطيرة للإفطار.", 2),
    ("Saft ist lecker.", "Juice is delicious.", "العصير لذيذ.", 1),
    ("Ich gehe oft ins Restaurant.", "I often go to the restaurant.", "أنا أذهب إلى المطعم في كثير من الأحيان.", 2),
    ("Die Suppe ist heiß.", "The soup is hot.", "الحساء ساخن.", 1),
    ("Ich mag Schokolade.", "I like chocolate.", "أنا أحب الشوكولاتة.", 1),
    ("Milch ist gut für Kinder.", "Milk is good for children.", "الحليب جيد للأطفال.", 2),
    ("Ich kaufe Lebensmittel im Supermarkt.", "I buy groceries at the supermarket.", "أنا أشتري البقالة في السوبر ماركت.", 2),
    ("Das Eis schmilzt schnell.", "The ice cream melts quickly.", "الآيس كريم يذوب بسرعة.", 2),
    ("Ich trinke kein Alkohol.", "I don't drink alcohol.", "أنا لا أشرب الكحول.", 1),
    ("Gemüse ist wichtig für die Ernährung.", "Vegetables are important for nutrition.", "الخضروات مهمة للتغذية.", 3),
    ("Ich esse gerne Nudeln.", "I like to eat pasta.", "أنا أحب أكل المعكرونة.", 1),
    ("Der Kaffee ist zu stark.", "The coffee is too strong.", "القهوة قوية جدًا.", 2),
    ("Ich koche für meine Familie.", "I cook for my family.", "أنا أطبخ لعائلتي.", 2),
    ("Das Bier ist kalt.", "The beer is cold.", "البيرة باردة.", 1),
    ("Ich trinke Wasser ohne Kohlensäure.", "I drink water without carbonation.", "أنا أشرب الماء بدون غاز.", 2),
    ("Die Zitrone ist sauer.", "The lemon is sour.", "الليمون حامض.", 1),
    ("Ich esse einen Apfel jeden Tag.", "I eat an apple every day.", "أنا أتناول تفاحة كل يوم.", 2),
    ("Das Restaurant hat gute Bewertungen.", "The restaurant has good reviews.", "المطعم له تقييمات جيدة.", 3),
    ("Ich mag italienisches Essen.", "I like Italian food.", "أنا أحب الطعام الإيطالي.", 2),
    ("Der Kuchen schmeckt herrlich.", "The cake tastes wonderful.", "الكعكة طعمها رائع.", 2),
    ("Ich trinke Orangensaft zum Frühstück.", "I drink orange juice for breakfast.", "أنا أشرب عصير البرتقال للإفطار.", 2),
    ("Frisches Brot ist am besten.", "Fresh bread is the best.", "الخبز الطازج هو الأفضل.", 2),
    ("Ich trinke gerne Saft.", "I like to drink juice.", "أنا أحب شرب العصير.", 1),
]

for f in food_a1:
    a1_sentences.append(f'    {{"german_text": "{f[0]}", "english_translation": "{f[1]}", "arabic_translation": "{f[2]}", "level": "A1", "difficulty_score": {f[3]}, "category": "Food & Drinks"}},')

# Shopping A1 (30)
shopping_a1 = [
    ("Ich gehe einkaufen.", "I go shopping.", "أنا أذهب للتسوق.", 1),
    ("Das Hemd kostet 20 Euro.", "The shirt costs 20 euros.", "القميص يكلف 20 يورو.", 2),
    ("Ich brauche neue Schuhe.", "I need new shoes.", "أحتاج إلى أحذية جديدة.", 1),
    ("Das ist zu teuer.", "That is too expensive.", "هذا باهظ الثمن.", 1),
    ("Ich kaufe ein Geschenk für meine Mutter.", "I buy a gift for my mother.", "أنا أشتري هدية لأمي.", 2),
    ("Die Jacke passt mir gut.", "The jacket fits me well.", "السترة تناسبني جيدًا.", 2),
    ("Ich bezahle mit Karte.", "I pay with card.", "أنا أدفع بالبطاقة.", 2),
    ("Der Supermarkt ist um die Ecke.", "The supermarket is around the corner.", "السوبر ماركت خلف الزاوية.", 2),
    ("Ich suche eine Hose.", "I am looking for pants.", "أنا أبحث عن بنطال.", 1),
    ("Das Angebot ist gut.", "The offer is good.", "العرض جيد.", 1),
    ("Ich kaufe Obst und Gemüse.", "I buy fruit and vegetables.", "أنا أشتري الفواكه والخضروات.", 2),
    ("Die Jeans sind im Angebot.", "The jeans are on sale.", "الجينز معروض للبيع.", 2),
    ("Ich habe die Quittung verloren.", "I lost the receipt.", "لقد فقدت الإيصال.", 2),
    ("Kann ich das umtauschen?", "Can I exchange this?", "هل يمكنني استبدال هذا؟", 2),
    ("Das Geschäft öffnet um 9 Uhr.", "The store opens at 9 o'clock.", "المتجر يفتح في الساعة 9.", 2),
    ("Ich brauche einen neuen Rucksack.", "I need a new backpack.", "أحتاج إلى حقيبة ظهر جديدة.", 2),
    ("Die Schuhe sind bequem.", "The shoes are comfortable.", "الأحذية مريحة.", 2),
    ("Ich kaufe ein Buch.", "I buy a book.", "أنا أشتري كتابًا.", 1),
    ("Das ist ein guter Preis.", "That is a good price.", "هذا سعر جيد.", 1),
    ("Ich gehe in die Mall.", "I go to the mall.", "أنا أذهب إلى المركز التجاري.", 1),
    ("Die Tasche ist schön.", "The bag is beautiful.", "الحقيبة جميلة.", 1),
    ("Ich habe nicht genug Geld.", "I don't have enough money.", "ليس لدي ما يكفي من المال.", 2),
    ("Kann ich mit Kreditkarte zahlen?", "Can I pay with credit card?", "هل يمكنني الدفع ببطاقة الائتمان؟", 3),
    ("Das Geschäft ist geschlossen.", "The store is closed.", "المتجر مغلق.", 1),
    ("Ich kaufe Geschenke für Weihnachten.", "I buy Christmas gifts.", "أنا أشتري هدايا عيد الميلاد.", 2),
    ("Die Bluse passt nicht.", "The blouse does not fit.", "البلوزة لا تناسب.", 2),
    ("Ich suche ein Geschenk für meinen Bruder.", "I am looking for a gift for my brother.", "أنا أبحث عن هدية لأخي.", 2),
    ("Das ist reduziert.", "That is reduced.", "هذا مخفض.", 1),
    ("Ich kaufe Milch und Eier.", "I buy milk and eggs.", "أنا أشتري الحليب والبيض.", 2),
    ("Der Verkäufer ist freundlich.", "The salesperson is friendly.", "مندوب المبيعات ودود.", 2),
]

for s in shopping_a1:
    a1_sentences.append(f'    {{"german_text": "{s[0]}", "english_translation": "{s[1]}", "arabic_translation": "{s[2]}", "level": "A1", "difficulty_score": {s[3]}, "category": "Shopping"}},')

# Directions A1 (30)
directions_a1 = [
    ("Wo ist der Bahnhof?", "Where is the train station?", "أين محطة القطار؟", 1),
    ("Gehen Sie geradeaus.", "Go straight ahead.", "اذهب مباشرة.", 1),
    ("Biegen Sie links ab.", "Turn left.", "انعطف يسارًا.", 1),
    ("Biegen Sie rechts ab.", "Turn right.", "انعطف يمينًا.", 1),
    ("Die Bank ist neben dem Supermarkt.", "The bank is next to the supermarket.", "البنك بجوار السوبر ماركت.", 2),
    ("Wie komme ich zum Flughafen?", "How do I get to the airport?", "كيف أصل إلى المطار؟", 2),
    ("Die Post ist gegenüber der Schule.", "The post office is opposite the school.", "مكتب البريد مقابل المدرسة.", 2),
    ("Gehen Sie über die Brücke.", "Go over the bridge.", "اذهب فوق الجسر.", 2),
    ("Die Straße heißt Hauptstraße.", "The street is called Main Street.", "الشارع يسمى الشارع الرئيسي.", 2),
    ("Wo ist die Toilette?", "Where is the toilet?", "أين المرحاض؟", 1),
    ("Die Apotheke ist um die Ecke.", "The pharmacy is around the corner.", "الصيدلية خلف الزاوية.", 2),
    ("Fahren Sie bis zur Ampel.", "Drive until the traffic light.", "اقود حتى إشارة المرور.", 2),
    ("Die Bibliothek ist hinter dem Rathaus.", "The library is behind the town hall.", "المكتبة خلف قاعة المدينة.", 3),
    ("Wo ist die nächste U-Bahn-Station?", "Where is the nearest subway station?", "أين أقرب محطة مترو؟", 3),
    ("Gehen Sie die Treppe hoch.", "Go up the stairs.", "اصعد الدرج.", 2),
    ("Die Haltestelle ist dort drüben.", "The stop is over there.", "الموقف هناك.", 2),
    ("Ich habe mich verlaufen.", "I got lost.", "لقد ضللت طريقي.", 2),
    ("Können Sie mir den Weg zeigen?", "Can you show me the way?", "هل يمكنك إرشادي إلى الطريق؟", 2),
    ("Die Kirche ist im Zentrum.", "The church is in the center.", "الكنيسة في المركز.", 2),
    ("Wo ist der Parkplatz?", "Where is the parking lot?", "أين موقف السيارات؟", 1),
    ("Fahren Sie nicht zu schnell.", "Don't drive too fast.", "لا تقود بسرعة كبيرة.", 2),
    ("Die Schule ist gegenüber dem Park.", "The school is opposite the park.", "المدرسة مقابل الحديقة.", 2),
    ("Gehen Sie durch den Park.", "Go through the park.", "اذهب عبر الحديقة.", 2),
    ("Die Adresse ist falsch.", "The address is wrong.", "العنوان خاطئ.", 2),
    ("Wo ist das Hotel?", "Where is the hotel?", "أين الفندق؟", 1),
    ("Die Bushaltestelle ist vor dem Haus.", "The bus stop is in front of the house.", "موقف الحافلة أمام المنزل.", 2),
    ("Ich brauche eine Karte.", "I need a map.", "أحتاج إلى خريطة.", 1),
    ("Die Stadtmauer ist alt.", "The city wall is old.", "سور المدينة قديم.", 2),
    ("Gehen Sie am Fluss entlang.", "Walk along the river.", "امشي على طول النهر.", 2),
    ("Die Polizeistation ist in der Nähe.", "The police station is nearby.", "مركز الشرطة قريب.", 2),
]

for d in directions_a1:
    a1_sentences.append(f'    {{"german_text": "{d[0]}", "english_translation": "{d[1]}", "arabic_translation": "{d[2]}", "level": "A1", "difficulty_score": {d[3]}, "category": "Directions"}},')

# Transport A1 (30)
transport_a1 = [
    ("Ich fahre mit dem Bus.", "I take the bus.", "أنا أستقل الحافلة.", 1),
    ("Die Bahn hat Verspätung.", "The train is delayed.", "القطار متأخر.", 2),
    ("Ich kaufe eine Fahrkarte.", "I buy a ticket.", "أنا أشتري تذكرة.", 1),
    ("Der Flug dauert zwei Stunden.", "The flight takes two hours.", "الرحلة تستغرق ساعتين.", 2),
    ("Ich nehme ein Taxi.", "I take a taxi.", "أنا أستقل سيارة أجرة.", 1),
    ("Das Fahrrad ist ein gutes Transportmittel.", "The bicycle is a good means of transport.", "الدراجة وسيلة نقل جيدة.", 3),
    ("Der Bus fährt alle 10 Minuten.", "The bus runs every 10 minutes.", "الحافلة تعمل كل 10 دقائق.", 2),
    ("Ich habe mein Fahrrad verloren.", "I lost my bicycle.", "لقد فقدت دراجتي.", 2),
    ("Die U-Bahn ist sehr schnell.", "The subway is very fast.", "المترو سريع جدًا.", 2),
    ("Ich fahre nach Berlin morgen.", "I drive to Berlin tomorrow.", "أنا أقود إلى برلين غدًا.", 2),
    ("Der Zug fährt um 8 Uhr ab.", "The train departs at 8 o'clock.", "القطار يغادر في الساعة 8.", 2),
    ("Ich brauche ein Fahrrad.", "I need a bicycle.", "أحتاج إلى دراجة.", 1),
    ("Das Auto ist kaputt.", "The car is broken.", "السيارة معطلة.", 1),
    ("Ich fliege nach Paris.", "I fly to Paris.", "أنا أطير إلى باريس.", 1),
    ("Die Fähre fährt zum Hafen.", "The ferry goes to the port.", "العبارة تذهب إلى الميناء.", 2),
    ("Ich steige am Hauptbahnhof aus.", "I get off at the main station.", "أنا أنزل في المحطة الرئيسية.", 2),
    ("Das Ticket ist teuer.", "The ticket is expensive.", "التذكرة باهظة الثمن.", 1),
    ("Ich nehme die S-Bahn.", "I take the S-Bahn.", "أنا أستقل الـ S-Bahn.", 2),
    ("Der Flughafen ist weit weg.", "The airport is far away.", "المطار بعيد.", 2),
    ("Ich fahre mit dem Motorrad.", "I ride a motorcycle.", "أنا أقود دراجة نارية.", 2),
    ("Die Straße ist gesperrt.", "The road is closed.", "الطريق مغلق.", 2),
    ("Ich habe ein Fahrrad gestohlen.", "I stole a bicycle.", "لقد سرقت دراجة.", 2),
    ("Der Bus kommt pünktlich.", "The bus arrives on time.", "الحافلة تصل في الموعد.", 2),
    ("Ich fahre mit dem Aufzug.", "I take the elevator.", "أنا أستقل المصعد.", 2),
    ("Die Rolltreppe ist defekt.", "The escalator is defective.", "السلم الكهربائي معطل.", 3),
    ("Ich nehme den Zug nach Hamburg.", "I take the train to Hamburg.", "أنا أستقل القطار إلى هامبورغ.", 2),
    ("Das Fahrrad ist rot.", "The bicycle is red.", "الدراجة حمراء.", 1),
    ("Ich fahre gerne Auto.", "I like to drive a car.", "أنا أحب قيادة السيارة.", 2),
    ("Der Taxifahrer ist freundlich.", "The taxi driver is friendly.", "سائق التاكسي ودود.", 2),
    ("Ich brauche eine Fahrkarte nach München.", "I need a ticket to Munich.", "أحتاج إلى تذكرة إلى ميونخ.", 2),
]

for t in transport_a1:
    a1_sentences.append(f'    {{"german_text": "{t[0]}", "english_translation": "{t[1]}", "arabic_translation": "{t[2]}", "level": "A1", "difficulty_score": {t[3]}, "category": "Transport"}},')

# Travel A1 (30)
travel_a1 = [
    ("Ich mache Urlaub in Italien.", "I go on vacation in Italy.", "أنا أقضي عطلة في إيطاليا.", 2),
    ("Das Hotel ist sehr schön.", "The hotel is very beautiful.", "الفندق جميل جدًا.", 2),
    ("Ich habe ein Zimmer reserviert.", "I reserved a room.", "لقد حجزت غرفة.", 2),
    ("Die Reise war toll.", "The trip was great.", "الرحلة كانت رائعة.", 1),
    ("Ich brauche einen Reisepass.", "I need a passport.", "أحتاج إلى جواز سفر.", 2),
    ("Das Flugzeug startet bald.", "The plane takes off soon.", "الطائرة تقلع قريبًا.", 2),
    ("Ich besuche die Sehenswürdigkeiten.", "I visit the sights.", "أنا أزور المعالم السياحية.", 3),
    ("Die Stadt ist wunderschön.", "The city is wonderful.", "المدينة رائعة.", 2),
    ("Ich mache Fotos.", "I take photos.", "أنا ألتقط الصور.", 1),
    ("Das Souvenir ist billig.", "The souvenir is cheap.", "التذكار رخيص.", 1),
    ("Ich gehe an den Strand.", "I go to the beach.", "أنا أذهب إلى الشاطئ.", 1),
    ("Die Touristeninformation ist dort.", "The tourist information is there.", "مكتب السياحة هناك.", 2),
    ("Ich brauche eine Reiseversicherung.", "I need travel insurance.", "أحتاج إلى تأمين سفر.", 3),
    ("Der Urlaub ist zu kurz.", "The vacation is too short.", "العطلة قصيرة جدًا.", 2),
    ("Ich fliege mit Lufthansa.", "I fly with Lufthansa.", "أنا أطير مع لوفتهانزا.", 2),
    ("Das Gepäck ist schwer.", "The luggage is heavy.", "الأمتعة ثقيلة.", 1),
    ("Ich miete ein Auto am Flughafen.", "I rent a car at the airport.", "أنا أستأجر سيارة في المطار.", 3),
    ("Die Insel ist klein.", "The island is small.", "الجزيرة صغيرة.", 1),
    ("Ich besuche ein Museum.", "I visit a museum.", "أنا أزور متحفًا.", 2),
    ("Ich schwimme im Meer.", "I swim in the sea.", "أنا أسبح في البحر.", 1),
    ("Die Berge sind beeindruckend.", "The mountains are impressive.", "الجبال مذهلة.", 2),
    ("Ich brauche eine Landkarte.", "I need a map.", "أحتاج إلى خريطة.", 1),
    ("Der Reiseführer ist hilfreich.", "The travel guide is helpful.", "دليل السفر مفيد.", 3),
    ("Ich trinke einen Cocktail am Pool.", "I drink a cocktail by the pool.", "أنا أشرب كوكتيلًا بجانب المسبح.", 3),
    ("Das Hotel hat einen Pool.", "The hotel has a pool.", "الفندق به مسبح.", 2),
    ("Ich besuche meine Freunde in Spanien.", "I visit my friends in Spain.", "أزور أصدقائي في إسبانيا.", 2),
    ("Die Reise dauert 5 Stunden.", "The journey takes 5 hours.", "الرحلة تستغرق 5 ساعات.", 2),
    ("Ich gehe wandern.", "I go hiking.", "أنا أذهب للمشي لمسافات طويلة.", 2),
    ("Die Stadtmauer ist historisch.", "The city wall is historic.", "سور المدينة تاريخي.", 3),
    ("Ich liebe Reisen.", "I love traveling.", "أنا أحب السفر.", 1),
]

for t in travel_a1:
    a1_sentences.append(f'    {{"german_text": "{t[0]}", "english_translation": "{t[1]}", "arabic_translation": "{t[2]}", "level": "A1", "difficulty_score": {t[3]}, "category": "Travel"}},')

# Time & Date A1 (30)
timedate_a1 = [
    ("Wie spät ist es?", "What time is it?", "كم الساعة؟", 1),
    ("Es ist 3 Uhr nachmittags.", "It is 3 o'clock in the afternoon.", "الساعة 3 بعد الظهر.", 2),
    ("Heute ist Montag.", "Today is Monday.", "اليوم الاثنين.", 1),
    ("Morgen ist Dienstag.", "Tomorrow is Tuesday.", "غدًا الثلاثاء.", 1),
    ("Der 1. Januar ist Neujahr.", "January 1st is New Year's Day.", "1 يناير هو رأس السنة.", 2),
    ("Ich habe am Wochenende frei.", "I am free on the weekend.", "أنا حر في عطلة نهاية الأسبوع.", 2),
    ("Der Termin ist um 10 Uhr.", "The appointment is at 10 o'clock.", "الموعد في الساعة 10.", 2),
    ("Wann kommst du nach Hause?", "When do you come home?", "متى تأتي إلى المنزل؟", 2),
    ("Ich arbeite von 9 bis 5.", "I work from 9 to 5.", "أنا أعمل من 9 إلى 5.", 2),
    ("Der Zug fährt um 18 Uhr.", "The train leaves at 6 PM.", "القطار يغادر في الساعة 6 مساءً.", 2),
    ("Heute ist der 5. Juni.", "Today is June 5th.", "اليوم 5 يونيو.", 2),
    ("Gestern war ich im Kino.", "Yesterday I was at the cinema.", "أمس كنت في السينما.", 2),
    ("Morgen fahre ich nach Berlin.", "Tomorrow I drive to Berlin.", "غدًا أقود إلى برلين.", 2),
    ("Die Uhr geht vor.", "The clock is fast.", "الساعة سريعة.", 2),
    ("Es ist schon spät.", "It is already late.", "الوقت متأخر بالفعل.", 1),
    ("Ich habe keine Zeit.", "I have no time.", "ليس لدي وقت.", 1),
    ("Der Kalender ist neu.", "The calendar is new.", "التقويم جديد.", 2),
    ("Wann hast du Geburtstag?", "When is your birthday?", "متى عيد ميلادك؟", 2),
    ("Mein Geburtstag ist im August.", "My birthday is in August.", "عيد ميلادي في أغسطس.", 2),
    ("Die Schule beginnt im September.", "School starts in September.", "المدرسة تبدأ في سبتمبر.", 2),
    ("Ich bleibe zwei Wochen.", "I stay for two weeks.", "أنا أبقى لمدة أسبوعين.", 2),
    ("Der Sommer ist heiß.", "Summer is hot.", "الصيف حار.", 1),
    ("Der Winter ist kalt.", "Winter is cold.", "الشتاء بارد.", 1),
    ("Es regnet oft im Herbst.", "It often rains in autumn.", "المطر كثير في الخريف.", 2),
    ("Der Frühling ist schön.", "Spring is beautiful.", "الربيع جميل.", 1),
    ("Ich feiere Silvester zu Hause.", "I celebrate New Year's Eve at home.", "أحتفل برأس السنة في المنزل.", 3),
    ("Die Uhrzeit ist 14:30.", "The time is 2:30 PM.", "الساعة 2:30 مساءً.", 2),
    ("Ich habe einen Termin beim Arzt.", "I have an appointment with the doctor.", "لدي موعد مع الطبيب.", 3),
    ("Wann fängt der Film an?", "When does the movie start?", "متى يبدأ الفيلم؟", 2),
    ("Ich warte seit einer Stunde.", "I have been waiting for an hour.", "أنا أنتظر منذ ساعة.", 3),
]

for t in timedate_a1:
    a1_sentences.append(f'    {{"german_text": "{t[0]}", "english_translation": "{t[1]}", "arabic_translation": "{t[2]}", "level": "A1", "difficulty_score": {t[3]}, "category": "Time & Date"}},')

# Weather A1 (30)
weather_a1 = [
    ("Es regnet heute.", "It is raining today.", "يمطر اليوم.", 1),
    ("Es schneit im Winter.", "It snows in winter.", "تتساقط الثلوج في الشتاء.", 2),
    ("Der Himmel ist blau.", "The sky is blue.", "السماء زرقاء.", 1),
    ("Es ist windig.", "It is windy.", "الجو عاصف.", 1),
    ("Die Temperatur ist 20 Grad.", "The temperature is 20 degrees.", "درجة الحرارة 20 درجة.", 2),
    ("Es ist neblig am Morgen.", "It is foggy in the morning.", "الجو ضبابي في الصباح.", 2),
    ("Gewitter kommen oft im Sommer.", "Thunderstorms often come in summer.", "العواصف الرعدية تأتي في كثير من الأحيان في الصيف.", 3),
    ("Es ist bewölkt.", "It is cloudy.", "الجو غائم.", 1),
    ("Die Sonne scheint.", "The sun is shining.", "الشمس تشرق.", 1),
    ("Es ist kalt draußen.", "It is cold outside.", "الجو بارد في الخارج.", 1),
    ("Der Regen hört auf.", "The rain stops.", "المطر يتوقف.", 2),
    ("Es ist heiß im Juli.", "It is hot in July.", "الجو حار في يوليو.", 2),
    ("Der Schnee ist tief.", "The snow is deep.", "الثلج عميق.", 1),
    ("Es taut jetzt.", "It is thawing now.", "الجليد يذوب الآن.", 2),
    ("Der Wind weht stark.", "The wind blows strongly.", "الرياح تهب بقوة.", 2),
    ("Es ist feucht heute.", "It is humid today.", "الجو رطب اليوم.", 2),
    ("Die Wolken ziehen vorbei.", "The clouds pass by.", "السحب تمر.", 2),
    ("Es friert in der Nacht.", "It freezes at night.", "الجو يتجمد في الليل.", 2),
    ("Der Regenbogen ist schön.", "The rainbow is beautiful.", "قوس قزح جميل.", 2),
    ("Es ist stürmisch.", "It is stormy.", "الجو عاصف.", 2),
    ("Die Temperatur steigt.", "The temperature rises.", "درجة الحرارة ترتفع.", 2),
    ("Es ist sonnig heute.", "It is sunny today.", "الجو مشمس اليوم.", 1),
    ("Der Herbst ist bunt.", "Autumn is colorful.", "الخريف ملون.", 2),
    ("Es hagelt.", "It is hailing.", "تتساقط البرد.", 2),
    ("Die Luft ist frisch.", "The air is fresh.", "الهواء نقي.", 2),
    ("Es ist schwül heute.", "It is muggy today.", "الجو خانق اليوم.", 2),
    ("Das Wetter ist wechselhaft.", "The weather is changeable.", "الطقس متقلب.", 3),
    ("Es ist frostig morgens.", "It is frosty in the morning.", "الجو صقيع في الصباح.", 2),
    ("Die Sonne geht unter.", "The sun sets.", "الشمس تغرب.", 2),
    ("Es ist angenehm draußen.", "It is pleasant outside.", "الجو لطيف في الخارج.", 2),
]

for w in weather_a1:
    a1_sentences.append(f'    {{"german_text": "{w[0]}", "english_translation": "{w[1]}", "arabic_translation": "{w[2]}", "level": "A1", "difficulty_score": {w[3]}, "category": "Weather"}},')

# Now build A2 sentences (400) - difficulty 2-4
a2_sentences = []

# Hobbies A2 (25)
hobbies_a2 = [
    ("Ich lese gerne Bücher in meiner Freizeit.", "I like to read books in my free time.", "أنا أحب قراءة الكتب في وقت فراغي.", 2),
    ("Ich spiele jeden Samstag Fußball mit Freunden.", "I play football with friends every Saturday.", "أنا ألعب كرة القدم مع الأصدقاء كل سبت.", 3),
    ("Mein Hobby ist Malen und Zeichnen.", "My hobby is painting and drawing.", "هوايتي هي الرسم والتلوين.", 2),
    ("Ich höre oft Musik, wenn ich koche.", "I often listen to music when I cook.", "أنا أستمع إلى الموسيقى في كثير من الأحيان عندما أطبخ.", 3),
    ("Ich gehe jeden Tag joggen.", "I go jogging every day.", "أنا أذهب للهرولة كل يوم.", 3),
    ("Ich sammle Briefmarken.", "I collect stamps.", "أنا أجمع الطوابع.", 2),
    ("Ich spiele Gitarre in meiner Freizeit.", "I play guitar in my free time.", "أنا أعزف الغيتار في وقت فراغي.", 3),
    ("Ich mache Yoga jeden Morgen.", "I do yoga every morning.", "أنا أمارس اليوغا كل صباح.", 3),
    ("Ich gehe gerne ins Kino.", "I like to go to the cinema.", "أنا أحب الذهاب إلى السينما.", 2),
    ("Ich fotografiere gerne Landschaften.", "I like to photograph landscapes.", "أنا أحب تصوير المناظر الطبيعية.", 3),
    ("Ich spiele Videospiele am Wochenende.", "I play video games on weekends.", "أنا ألعب ألعاب الفيديو في عطلات نهاية الأسبوع.", 3),
    ("Ich gehe schwimmen im Sommer.", "I go swimming in summer.", "أنا أذهب للسباحة في الصيف.", 2),
    ("Ich mache gerne Wandern im Wald.", "I like to hike in the forest.", "أنا أحب المشي لمسافات طويلة في الغابة.", 3),
    ("Ich schreibe Gedichte in meiner Freizeit.", "I write poems in my free time.", "أنا أكتب القصائد في وقت فراغي.", 3),
    ("Ich bastle gerne Dinge mit Holz.", "I like to craft things with wood.", "أنا أحب صنع الأشياء بالخشب.", 3),
    ("Ich spiele Schach mit meinem Vater.", "I play chess with my father.", "أنا ألعب الشطرنج مع أبي.", 3),
    ("Ich gehe tanzen am Freitagabend.", "I go dancing on Friday evening.", "أنا أذهب للرقص مساء الجمعة.", 3),
    ("Ich lese Zeitungen jeden Morgen.", "I read newspapers every morning.", "أنا أقرأ الصحف كل صباح.", 3),
    ("Ich lerne gerne neue Sprachen.", "I like to learn new languages.", "أنا أحب تعلم لغات جديدة.", 3),
    ("Ich koche gerne für Gäste.", "I like to cook for guests.", "أنا أحب الطبخ للضيوف.", 3),
    ("Ich reite gerne Pferde.", "I like to ride horses.", "أنا أحب ركوب الخيل.", 3),
    ("Ich mache Kampfsport zweimal pro Woche.", "I do martial arts twice a week.", "أنا أمارس فنون القتال مرتين في الأسبوع.", 4),
    ("Ich sammle alte Münzen.", "I collect old coins.", "أنا أجمع العملات القديمة.", 2),
    ("Ich gehe Angeln am Wochenende.", "I go fishing on weekends.", "أنا أذهب للصيد في عطلات نهاية الأسبوع.", 3),
    ("Ich mache gerne Fahrradtouren.", "I like to go on bicycle tours.", "أنا أحب الرحلات بالدراجة.", 3),
]

for h in hobbies_a2:
    a2_sentences.append(f'    {{"german_text": "{h[0]}", "english_translation": "{h[1]}", "arabic_translation": "{h[2]}", "level": "A2", "difficulty_score": {h[3]}, "category": "Hobbies"}},')

# Education A2 (25)
education_a2 = [
    ("Ich gehe zur Grundschule.", "I go to elementary school.", "أنا أذهب إلى المدرسة الابتدائية.", 2),
    ("Ich lerne Mathe und Deutsch in der Schule.", "I learn math and German in school.", "أنا أتعلم الرياضيات والألمانية في المدرسة.", 3),
    ("Die Schule beginnt um 8 Uhr.", "School starts at 8 o'clock.", "المدرسة تبدأ في الساعة 8.", 2),
    ("Ich habe Hausaufgaben für morgen.", "I have homework for tomorrow.", "لدي واجبات منزلية لغدًا.", 2),
    ("Ich lerne für die Prüfung.", "I study for the exam.", "أنا أدرس من أجل الامتحان.", 2),
    ("Der Lehrer erklärt das Thema.", "The teacher explains the topic.", "المعلم يشرح الموضوع.", 2),
    ("Ich schreibe einen Aufsatz über meine Familie.", "I write an essay about my family.", "أنا أكتب مقالًا عن عائلتي.", 3),
    ("Die Universität ist groß.", "The university is big.", "الجامعة كبيرة.", 2),
    ("Ich studiere Betriebswirtschaft.", "I study business administration.", "أنا أدرس إدارة الأعمال.", 3),
    ("Ich lerne Programmieren in meiner Freizeit.", "I learn programming in my free time.", "أنا أتعلم البرمجة في وقت فراغي.", 4),
    ("Die Bibliothek hat viele Bücher.", "The library has many books.", "المكتبة تحتوي على الكثير من الكتب.", 2),
    ("Ich nehme an einem Deutschkurs teil.", "I participate in a German course.", "أنا أشارك في دورة ألمانية.", 3),
    ("Der Unterricht dauert 45 Minuten.", "The class lasts 45 minutes.", "الحصة تستغرق 45 دقيقة.", 3),
    ("Ich habe eine gute Note in Englisch.", "I have a good grade in English.", "لدي درجة جيدة في الإنجليزية.", 3),
    ("Ich lerne Vokabeln jeden Tag.", "I learn vocabulary every day.", "أنا أتعلم المفردات كل يوم.", 3),
    ("Die Schule hat einen großen Hof.", "The school has a large courtyard.", "المدرسة لها ساحة كبيرة.", 2),
    ("Ich mache eine Ausbildung als Krankenpfleger.", "I do an apprenticeship as a nurse.", "أنا أتدرب كممرض.", 4),
    ("Ich schreibe eine Prüfung nächste Woche.", "I take an exam next week.", "أنا أجتاز امتحانًا الأسبوع القادم.", 3),
    ("Die Lehrerin ist sehr nett.", "The teacher is very nice.", "المعلمة لطيفة جدًا.", 2),
    ("Ich lerne Geschichte und Geografie.", "I learn history and geography.", "أنا أتعلم التاريخ والجغرافيا.", 3),
    ("Ich besuche eine Sprachschule.", "I attend a language school.", "أنا أحضر مدرسة لغات.", 3),
    ("Die Klasse hat 25 Schüler.", "The class has 25 students.", "الفصل به 25 طالبًا.", 3),
    ("Ich lerne Grammatik mit einem Buch.", "I learn grammar with a book.", "أنا أتعلم القواعد بكتاب.", 3),
    ("Ich mache einen Computerkurs.", "I take a computer course.", "أنا أحضر دورة كمبيوتر.", 3),
    ("Ich lerne fleißig für die Schule.", "I study diligently for school.", "أنا أدرس بجد للمدرسة.", 3),
]

for e in education_a2:
    a2_sentences.append(f'    {{"german_text": "{e[0]}", "english_translation": "{e[1]}", "arabic_translation": "{e[2]}", "level": "A2", "difficulty_score": {e[3]}, "category": "Education"}},')

# Daily Life A2 (25)
daily_a2 = [
    ("Ich stehe um 7 Uhr auf.", "I get up at 7 o'clock.", "أنا أستيقظ في الساعة 7.", 2),
    ("Ich bürste meine Zähne morgens und abends.", "I brush my teeth morning and evening.", "أنا أفرش أسناني صباحًا ومساءً.", 3),
    ("Ich frühstücke um 8 Uhr.", "I have breakfast at 8 o'clock.", "أنا أتناول الإفطار في الساعة 8.", 2),
    ("Ich fahre mit dem Bus zur Arbeit.", "I take the bus to work.", "أنا أستقل الحافلة إلى العمل.", 3),
    ("Ich mache die Wohnung sauber am Samstag.", "I clean the apartment on Saturday.", "أنا أنظف الشقة يوم السبت.", 3),
    ("Ich kaufe Lebensmittel nach der Arbeit.", "I buy groceries after work.", "أنا أشتري البقالة بعد العمل.", 3),
    ("Ich koche das Abendessen für meine Familie.", "I cook dinner for my family.", "أنا أطبخ العشاء لعائلتي.", 3),
    ("Ich sehe fern nach dem Abendessen.", "I watch TV after dinner.", "أنا أشاهد التلفاز بعد العشاء.", 3),
    ("Ich gehe um 10 Uhr ins Bett.", "I go to bed at 10 o'clock.", "أنا أذهب إلى السرير في الساعة 10.", 2),
    ("Ich wasche meine Kleidung am Wochenende.", "I wash my clothes on weekends.", "أنا أغسل ملابسي في عطلات نهاية الأسبوع.", 3),
    ("Ich trinke Kaffee vor der Arbeit.", "I drink coffee before work.", "أنا أشرب القهوة قبل العمل.", 2),
    ("Ich treffe meine Freunde am Abend.", "I meet my friends in the evening.", "أنا ألتقي أصدقائي في المساء.", 3),
    ("Ich räume mein Zimmer jeden Tag auf.", "I tidy my room every day.", "أنا أنظف غرفتي كل يوم.", 3),
    ("Ich gehe spazieren im Park.", "I go for a walk in the park.", "أنا أذهب للتمشية في الحديقة.", 3),
    ("Ich mache Sport zweimal pro Woche.", "I do sports twice a week.", "أنا أمارس الرياضة مرتين في الأسبوع.", 3),
    ("Ich telefoniere mit meiner Mutter.", "I talk on the phone with my mother.", "أنا أتحدث عبر الهاتف مع أمي.", 3),
    ("Ich putze die Wohnung jeden Samstag.", "I clean the apartment every Saturday.", "أنا أنظف الشقة كل سبت.", 3),
    ("Ich bügle meine Hemden am Sonntag.", "I iron my shirts on Sunday.", "أنا أكوي قمصاني يوم الأحد.", 3),
    ("Ich gehe jeden Tag zur Arbeit.", "I go to work every day.", "أنا أذهب إلى العمل كل يوم.", 2),
    ("Ich koche ein festliches Essen.", "I cook a festive meal.", "أنا أطبخ وجبة احتفالية.", 3),
    ("Ich lese vor dem Schlafen ein Buch.", "I read a book before sleeping.", "أنا أقرأ كتابًا قبل النوم.", 3),
    ("Ich trinke einen Tee abends.", "I drink a tea in the evening.", "أنا أشرب شايًا في المساء.", 2),
    ("Ich mache einen Spaziergang am See.", "I take a walk by the lake.", "أنا أتمشى بجانب البحيرة.", 3),
    ("Ich höre Nachrichten im Radio.", "I listen to news on the radio.", "أنا أستمع للأخبار في الراديو.", 3),
    ("Ich gehe jeden Montag zum Fitnessstudio.", "I go to the fitness studio every Monday.", "أنا أذهب للنادي الرياضي كل اثنين.", 4),
]

for d in daily_a2:
    a2_sentences.append(f'    {{"german_text": "{d[0]}", "english_translation": "{d[1]}", "arabic_translation": "{d[2]}", "level": "A2", "difficulty_score": {d[3]}, "category": "Daily Life"}},')

# Feelings A2 (25)
feelings_a2 = [
    ("Ich bin glücklich heute.", "I am happy today.", "أنا سعيد اليوم.", 2),
    ("Ich fühle mich müde nach der Arbeit.", "I feel tired after work.", "أنا أشعر بالتعب بعد العمل.", 3),
    ("Es macht mir Spaß, Deutsch zu lernen.", "It is fun for me to learn German.", "تعلم الألمانية ممتع بالنسبة لي.", 3),
    ("Ich bin traurig wegen der Nachricht.", "I am sad because of the news.", "أنا حزين بسبب الأخبار.", 3),
    ("Ich habe Angst vor dem Examen.", "I am afraid of the exam.", "أنا خائف من الامتحان.", 3),
    ("Ich bin stolz auf meine Leistung.", "I am proud of my achievement.", "أنا فخور بإنجازي.", 3),
    ("Ich ärgere mich über den Verkehr.", "I am annoyed by the traffic.", "أنا منزعج من الزحام.", 3),
    ("Ich bin wütend auf meinen Bruder.", "I am angry at my brother.", "أنا غاضب على أخي.", 3),
    ("Ich fühle mich entspannt am Wochenende.", "I feel relaxed on weekends.", "أنا أشعر بالاسترخاء في عطلات نهاية الأسبوع.", 4),
    ("Ich bin begeistert von der Musik.", "I am enthusiastic about the music.", "أنا متحمس للموسيقى.", 3),
    ("Ich habe Sehnsucht nach Hause.", "I feel homesick.", "أنا أشعر بالحنين إلى المنزل.", 3),
    ("Ich bin nervös vor der Präsentation.", "I am nervous before the presentation.", "أنا عصبي قبل العرض التقديمي.", 3),
    ("Ich fühle mich einsam ohne Freunde.", "I feel lonely without friends.", "أنا أشعر بالوحدة بدون أصدقاء.", 3),
    ("Ich bin dankbar für die Hilfe.", "I am grateful for the help.", "أنا ممتن للمساعدة.", 3),
    ("Ich bin verliebt in meine Nachbarin.", "I am in love with my neighbor.", "أنا أحب جارتي.", 3),
    ("Ich fühle mich gesund und fit.", "I feel healthy and fit.", "أنا أشعر بالصحة واللياقة.", 3),
    ("Ich bin enttäuscht von dem Film.", "I am disappointed with the movie.", "أنا خائب الأمل من الفيلم.", 3),
    ("Ich habe Lust auf Pizza heute.", "I feel like eating pizza today.", "أنا أرغب في أكل البيتزا اليوم.", 3),
    ("Ich bin gelangweilt im Unterricht.", "I am bored in class.", "أنا أشعر بالملل في الفصل.", 3),
    ("Ich freue mich auf das Wochenende.", "I look forward to the weekend.", "أنا أتطلع لعطلة نهاية الأسبوع.", 3),
    ("Ich bin schüchtern bei fremden Leuten.", "I am shy with strangers.", "أنا خجول مع الغرباء.", 3),
    ("Ich fühle mich sicher in der Stadt.", "I feel safe in the city.", "أنا أشعر بالأمان في المدينة.", 3),
    ("Ich bin neidisch auf meinen Kollegen.", "I am jealous of my colleague.", "أنا أحسد زميلي.", 3),
    ("Ich habe Mitleid mit dem Hund.", "I feel pity for the dog.", "أنا أشفق على الكلب.", 3),
    ("Ich bin optimistisch für die Zukunft.", "I am optimistic about the future.", "أنا متفائل بشأن المستقبل.", 4),
]

for f in feelings_a2:
    a2_sentences.append(f'    {{"german_text": "{f[0]}", "english_translation": "{f[1]}", "arabic_translation": "{f[2]}", "level": "A2", "difficulty_score": {f[3]}, "category": "Feelings"}},')

# Nature A2 (25)
nature_a2 = [
    ("Der Wald ist im Herbst sehr schön.", "The forest is very beautiful in autumn.", "الغابة جميلة جدًا في الخريف.", 3),
    ("Ich sehe viele Vögel im Garten.", "I see many birds in the garden.", "أنا أرى الكثير من الطيور في الحديقة.", 3),
    ("Die Blumen blühen im Frühling.", "The flowers bloom in spring.", "الزهور تتفتح في الربيع.", 3),
    ("Der Fluss fließt ruhig durch die Stadt.", "The river flows calmly through the city.", "النهر يتدفق بهدوء عبر المدينة.", 4),
    ("Ich sammle Steine am Strand.", "I collect stones on the beach.", "أنا أجمع الحجارة على الشاطئ.", 3),
    ("Die Sonne wärmt meine Haut.", "The sun warms my skin.", "الشمس تدفي بشرتي.", 3),
    ("Der Mond scheint hell in der Nacht.", "The moon shines bright in the night.", "القمر يضيء بريقًا في الليل.", 3),
    ("Ich beobachte die Sterne am Himmel.", "I observe the stars in the sky.", "أنا أراقب النجوم في السماء.", 3),
    ("Der See ist tief und dunkel.", "The lake is deep and dark.", "البحيرة عميقة ومظلمة.", 3),
    ("Die Bäume verlieren ihre Blätter.", "The trees lose their leaves.", "الأشجار تفقد أوراقها.", 3),
    ("Ich höre das Rauschen des Meeres.", "I hear the roar of the sea.", "أنا أسمع هدير البحر.", 3),
    ("Der Wasserfall ist beeindruckend.", "The waterfall is impressive.", "شلال الماء مذهل.", 3),
    ("Ich gehe spazieren im Regen.", "I go for a walk in the rain.", "أنا أتمشى تحت المطر.", 3),
    ("Die Luft riecht nach Wald.", "The air smells like forest.", "الهواء تفوح منه رائحة الغابة.", 3),
    ("Ich pflücke Beeren im Wald.", "I pick berries in the forest.", "أنا أقطف التوت في الغابة.", 3),
    ("Der Berggipfel ist mit Schnee bedeckt.", "The mountain peak is covered with snow.", "قمة الجبل مغطاة بالثلج.", 4),
    ("Ich sehe Rehe am Waldrand.", "I see deer at the edge of the forest.", "أنا أرى الغزلان عند حافة الغابة.", 4),
    ("Die Wiese ist voller Blumen.", "The meadow is full of flowers.", "المرج ممتلئ بالزهور.", 3),
    ("Ich mache ein Picknick im Park.", "I have a picnic in the park.", "أنا أقوم بنزهة في الحديقة.", 3),
    ("Der Nebel hängt über dem Tal.", "The fog hangs over the valley.", "الضباب يعلق فوق الوادي.", 3),
    ("Ich füttere die Enten am Teich.", "I feed the ducks at the pond.", "أنا أطعم البط عند البركة.", 3),
    ("Die Natur ist wunderschön hier.", "Nature is wonderful here.", "الطبيعة رائعة هنا.", 3),
    ("Ich sammle Muscheln am Strand.", "I collect shells on the beach.", "أنا أجمع الأصداف على الشاطئ.", 3),
    ("Der Regenbogen erscheint nach dem Regen.", "The rainbow appears after the rain.", "قوس قزح يظهر بعد المطر.", 3),
    ("Ich genieße die Ruhe im Wald.", "I enjoy the peace in the forest.", "أنا أستمتع بالهدوء في الغابة.", 4),
]

for n in nature_a2:
    a2_sentences.append(f'    {{"german_text": "{n[0]}", "english_translation": "{n[1]}", "arabic_translation": "{n[2]}", "level": "A2", "difficulty_score": {n[3]}, "category": "Nature"}},')

# Clothing A2 (25)
clothing_a2 = [
    ("Ich trage heute einen Pullover.", "I wear a sweater today.", "أنا أرتدي كنزة صوفية اليوم.", 2),
    ("Die Jacke passt perfekt zu meiner Hose.", "The jacket fits perfectly with my pants.", "السترة تناسب بنطالي تمامًا.", 3),
    ("Ich brauche einen neuen Mantel für den Winter.", "I need a new coat for winter.", "أحتاج إلى معطف جديد للشتاء.", 3),
    ("Diese Schuhe sind sehr bequem.", "These shoes are very comfortable.", "هذه الأحذية مريحة جدًا.", 3),
    ("Ich ziehe mich warm an im Winter.", "I dress warmly in winter.", "أنا أرتدي ملابس دافئة في الشتاء.", 3),
    ("Das Hemd muss gebügelt werden.", "The shirt needs to be ironed.", "القميص يحتاج إلى الكي.", 3),
    ("Ich kaufe einen Hut gegen die Sonne.", "I buy a hat against the sun.", "أنا أشتري قبعة ضد الشمس.", 3),
    ("Die Jeans sind zu eng für mich.", "The jeans are too tight for me.", "الجينز ضيقة جدًا بالنسبة لي.", 3),
    ("Ich trage gerne farbenfrohe Kleidung.", "I like to wear colorful clothing.", "أنا أحب ارتداء ملابس ملونة.", 4),
    ("Der Gürtel passt nicht zu den Schuhen.", "The belt does not match the shoes.", "الحزام لا يناسب الأحذية.", 3),
    ("Ich wasche meine Kleidung bei 40 Grad.", "I wash my clothes at 40 degrees.", "أنا أغسل ملابسي عند 40 درجة.", 3),
    ("Die Strumpfhose hat ein Loch.", "The tights have a hole.", "الجوارب الطويلة بها ثقب.", 3),
    ("Ich brauche neue Socken.", "I need new socks.", "أحتاج إلى جوارب جديدة.", 2),
    ("Das Kleid ist elegant und schick.", "The dress is elegant and chic.", "الفستان أنيق وعصري.", 3),
    ("Ich trage lieber Sportkleidung.", "I prefer to wear sportswear.", "أنا أفضل ارتداء ملابس رياضية.", 3),
    ("Der Schal schützt vor dem kalten Wind.", "The scarf protects from the cold wind.", "الوشاح يحمي من الرياح الباردة.", 4),
    ("Ich kaufe eine Winterjacke mit Fell.", "I buy a winter jacket with fur.", "أنا أشتري سترة شتوية بالفرو.", 3),
    ("Die Stiefel sind wasserdicht.", "The boots are waterproof.", "الحذاء العالي مضاد للماء.", 3),
    ("Ich habe meine Lieblingsbluse verloren.", "I lost my favorite blouse.", "أنا فقدت بلوزتي المفضلة.", 3),
    ("Die Farbe des T-Shirts ist verblichen.", "The color of the T-shirt is faded.", "لون التيشيرت بهت.", 3),
    ("Ich trage eine Brille seit meiner Kindheit.", "I wear glasses since my childhood.", "أنا أرتدي نظارة منذ طفولتي.", 3),
    ("Die Handschuhe passen in die Jackentasche.", "The gloves fit in the jacket pocket.", "القفازات تناسب جيب السترة.", 3),
    ("Ich brauche einen Anzug für die Arbeit.", "I need a suit for work.", "أحتاج إلى بدلة للعمل.", 3),
    ("Das Nachthemd ist aus Baumwolle.", "The nightgown is made of cotton.", "ثوب النوم مصنوع من القطن.", 3),
    ("Ich ziehe mich schnell an.", "I get dressed quickly.", "أنا أرتدي ملابسي بسرعة.", 2),
]

for c in clothing_a2:
    a2_sentences.append(f'    {{"german_text": "{c[0]}", "english_translation": "{c[1]}", "arabic_translation": "{c[2]}", "level": "A2", "difficulty_score": {c[3]}, "category": "Clothing"}},')

# Work A2 (25)
work_a2 = [
    ("Ich arbeite in einem Büro in der Stadt.", "I work in an office in the city.", "أنا أعمل في مكتب في المدينة.", 3),
    ("Mein Chef ist sehr nett und freundlich.", "My boss is very nice and friendly.", "مديري لطيف وودود جدًا.", 3),
    ("Ich habe einen stressigen Job.", "I have a stressful job.", "لدي وظيفة مجهدة.", 3),
    ("Ich arbeite montags bis freitags.", "I work Monday to Friday.", "أنا أعمل من الاثنين إلى الجمعة.", 3),
    ("Das Gehalt wird jeden Monat überwiesen.", "The salary is transferred every month.", "الراتب يحول كل شهر.", 3),
    ("Ich habe einen wichtigen Termin heute.", "I have an important appointment today.", "لدي موعد مهم اليوم.", 3),
    ("Meine Kollegen sind sehr hilfsbereit.", "My colleagues are very helpful.", "زملائي متعاونون جدًا.", 3),
    ("Ich schreibe E-Mails den ganzen Tag.", "I write emails all day long.", "أنا أكتب رسائل إلكترونية طوال اليوم.", 4),
    ("Die Besprechung dauert eine Stunde.", "The meeting lasts one hour.", "الاجتماع يستغرق ساعة واحدة.", 3),
    ("Ich bekomme vier Wochen Urlaub im Jahr.", "I get four weeks of vacation per year.", "أنا أحصل على أربعة أسابيع إجازة سنويًا.", 4),
    ("Ich benutze den Computer für meine Arbeit.", "I use the computer for my work.", "أنا أستخدم الكمبيوتر لعملي.", 3),
    ("Die Firma hat hundert Mitarbeiter.", "The company has a hundred employees.", "الشركة لديها مائة موظف.", 3),
    ("Ich suche eine neue Arbeitsstelle.", "I am looking for a new job.", "أنا أبحث عن وظيفة جديدة.", 3),
    ("Mein Büro ist im dritten Stock.", "My office is on the third floor.", "مكتبي في الطابق الثالث.", 3),
    ("Ich habe eine Gehaltserhöhung bekommen.", "I got a salary increase.", "لقد حصلت على زيادة في الراتب.", 4),
    ("Wir haben eine Kaffeepause um 11 Uhr.", "We have a coffee break at 11 o'clock.", "لدينا فاصل قهوة في الساعة 11.", 3),
    ("Ich arbeite als Softwareentwickler.", "I work as a software developer.", "أنا أعمل كمطور برمجيات.", 4),
    ("Die Arbeitszeit ist flexibel hier.", "The working hours are flexible here.", "ساعات العمل مرنة هنا.", 3),
    ("Ich habe Überstunden gemacht.", "I did overtime.", "أنا قمت بعمل إضافي.", 3),
    ("Der Arbeitsvertrag ist unterschrieben.", "The employment contract is signed.", "عقد العمل موقع.", 3),
    ("Ich fahre mit dem Aufzug ins fünfte Stockwerk.", "I take the elevator to the fifth floor.", "أنا أستقل المصعد إلى الطابق الخامس.", 4),
    ("Mein Schreibtisch ist ordentlich und sauber.", "My desk is tidy and clean.", "مكتبي مرتب ونظيف.", 3),
    ("Ich lerne neue Programme für die Arbeit.", "I learn new programs for work.", "أنا أتعلم برامج جديدة للعمل.", 4),
    ("Die Firma bietet Weiterbildungen an.", "The company offers further training.", "الشركة تقدم تدريبًا إضافيًا.", 4),
    ("Ich bin seit fünf Jahren in dieser Firma.", "I have been in this company for five years.", "أنا في هذه الشركة منذ خمس سنوات.", 4),
]

for w in work_a2:
    a2_sentences.append(f'    {{"german_text": "{w[0]}", "english_translation": "{w[1]}", "arabic_translation": "{w[2]}", "level": "A2", "difficulty_score": {w[3]}, "category": "Work"}},')

# Health A2 (25)
health_a2 = [
    ("Ich habe Halsschmerzen heute.", "I have a sore throat today.", "أنا لدي آلام في الحلق اليوم.", 3),
    ("Der Arzt verschreibt mir ein Medikament.", "The doctor prescribes me a medication.", "الطبيب يصف لي دواءً.", 3),
    ("Ich muss ins Krankenhaus zur Untersuchung.", "I have to go to the hospital for examination.", "يجب أن أذهب للمستشفى للفحص.", 4),
    ("Ich fühle mich nicht wohl.", "I don't feel well.", "أنا لا أشعر بالراحة.", 2),
    ("Ich habe Fieber seit gestern.", "I have had a fever since yesterday.", "لدي حرارة منذ أمس.", 3),
    ("Die Tabletten helfen gegen die Schmerzen.", "The pills help against the pain.", "الحبوب تساعد ضد الألم.", 3),
    ("Ich gehe zum Zahnarzt morgen.", "I go to the dentist tomorrow.", "أنا أذهب لطبيب الأسنان غدًا.", 3),
    ("Ich brauche eine Spritze gegen die Grippe.", "I need an injection against the flu.", "أحتاج إلى حقنة ضد الإنفلونزا.", 4),
    ("Ich treibe Sport, um fit zu bleiben.", "I do sports to stay fit.", "أنا أمارس الرياضة لأبقى لائقًا.", 4),
    ("Ich habe mich beim Joggen verletzt.", "I injured myself while jogging.", "أنا أصبت نفسي أثناء الهرولة.", 4),
    ("Die Wunde muss verbunden werden.", "The wound needs to be bandaged.", "الجرح يحتاج إلى تضميد.", 3),
    ("Ich habe eine Allergie gegen Pollen.", "I have an allergy to pollen.", "لدي حساسية ضد حبوب اللقاح.", 4),
    ("Ich ernähre mich gesund und ausgewogen.", "I eat healthily and balanced.", "أنا أتغذى بشكل صحي ومتوازن.", 4),
    ("Ich schlafe acht Stunden jede Nacht.", "I sleep eight hours every night.", "أنا أنام ثمان ساعات كل ليلة.", 3),
    ("Ich habe Kopfschmerzen nach der Arbeit.", "I have a headache after work.", "لدي ألم في الرأس بعد العمل.", 3),
    ("Ich gehe zur Massage einmal pro Woche.", "I go for a massage once a week.", "أنا أذهب للتدليك مرة في الأسبوع.", 4),
    ("Ich rauche nicht, weil es ungesund ist.", "I don't smoke because it is unhealthy.", "أنا لا أدخن لأنه غير صحي.", 4),
    ("Ich habe einen Termin beim Orthopäden.", "I have an appointment with the orthopedist.", "لدي موعد مع طبيب العظام.", 4),
    ("Ich trinke zweieinhalb Liter Wasser täglich.", "I drink two and a half liters of water daily.", "أنا أشرب لترين ونصف من الماء يوميًا.", 4),
    ("Ich habe Sodbrennen nach dem Essen.", "I have heartburn after eating.", "لدي حرقة في المعدة بعد الأكل.", 4),
    ("Ich nehme Vitamine jeden Morgen.", "I take vitamins every morning.", "أنا آخذ الفيتامينات كل صباح.", 3),
    ("Ich mache Dehnübungen vor dem Sport.", "I do stretching exercises before sports.", "أنا أقوم بتمارين الإطالة قبل الرياضة.", 4),
    ("Ich habe eine Erkältung im Winter.", "I have a cold in winter.", "لدي نزلة في الشتاء.", 3),
    ("Ich gehe zur Vorsorgeuntersuchung.", "I go for a preventive checkup.", "أنا أذهب للفحص الوقائي.", 4),
    ("Ich fühle mich wieder gesund nach der Kur.", "I feel healthy again after the cure.", "أنا أشعر بالصحة مجددًا بعد العلاج.", 4),
]

for h in health_a2:
    a2_sentences.append(f'    {{"german_text": "{h[0]}", "english_translation": "{h[1]}", "arabic_translation": "{h[2]}", "level": "A2", "difficulty_score": {h[3]}, "category": "Health"}},')

# Technology A2 (25)
tech_a2 = [
    ("Ich benutze ein Smartphone seit zwei Jahren.", "I have been using a smartphone for two years.", "أنا أستخدم هاتفًا ذكيًا منذ سنتين.", 4),
    ("Das Internet ist sehr wichtig für meine Arbeit.", "The internet is very important for my work.", "الإنترنت مهم جدًا لعملي.", 3),
    ("Ich sende eine E-Mail an meinen Chef.", "I send an email to my boss.", "أنا أرسل رسالة إلكترونية إلى مديري.", 3),
    ("Das Passwort muss mindestens acht Zeichen haben.", "The password must have at least eight characters.", "كلمة المرور يجب أن تحتوي على ثمانية رموز على الأقل.", 4),
    ("Ich lade die App aus dem Store herunter.", "I download the app from the store.", "أنا أحمل التطبيق من المتجر.", 4),
    ("Der Computer hat eine langsamer geworden.", "The computer has become slower.", "الكمبيوتر أصبح أبطأ.", 3),
    ("Ich speichere meine Dateien in der Cloud.", "I save my files in the cloud.", "أنا أحفظ ملفاتي في السحابة.", 4),
    ("Die Webseite lädt sehr langsam.", "The website loads very slowly.", "الموقع الإلكتروني يحمل ببطء شديد.", 4),
    ("Ich folge vielen Seiten in sozialen Medien.", "I follow many pages on social media.", "أنا أتابع الكثير من الصفحات في وسائل التواصل.", 4),
    ("Das Navigationssystem zeigt den Weg.", "The navigation system shows the way.", "نظام الملاحة يوضح الطريق.", 4),
    ("Ich chate mit meinen Freunden über WhatsApp.", "I chat with my friends via WhatsApp.", "أنا أدردش مع أصدقائي عبر واتساب.", 3),
    ("Die Batterie des Handys ist leer.", "The cell phone battery is empty.", "بطارية الهاتف فارغة.", 3),
    ("Ich suche Informationen im Internet.", "I search for information on the internet.", "أنا أبحث عن معلومات في الإنترنت.", 3),
    ("Ich erstelle ein Dokument auf dem Laptop.", "I create a document on the laptop.", "أنا أنشئ وثيقة على الحاسوب المحمول.", 4),
    ("Das WLAN funktioniert nicht im Wohnzimmer.", "The Wi-Fi does not work in the living room.", "الواي فاي لا يعمل في غرفة المعيشة.", 4),
    ("Ich nutze Google Maps für die Navigation.", "I use Google Maps for navigation.", "أنا أستخدم خرائط جوجل للملاحة.", 4),
    ("Ich habe einen Drucker zu Hause.", "I have a printer at home.", "لدي طابعة في المنزل.", 2),
    ("Die Software muss aktualisiert werden.", "The software needs to be updated.", "البرمجيات يجب تحديثها.", 4),
    ("Ich schaue Videos auf YouTube.", "I watch videos on YouTube.", "أنا أشاهد الفيديوهات على يوتيوب.", 3),
    ("Ich poste ein Foto auf Instagram.", "I post a photo on Instagram.", "أنا أنشر صورة على إنستغرام.", 3),
    ("Der Bildschirm ist kaputt gegangen.", "The screen broke.", "الشاشة انكسرت.", 3),
    ("Ich sichere meine Daten regelmäßig.", "I back up my data regularly.", "أنا أحفظ بياناتي بانتظام.", 4),
    ("Ich nutze ein Tablet für meine Arbeit.", "I use a tablet for my work.", "أنا أستخدم جهاز لوحيًا لعملي.", 4),
    ("Die Tastatur funktioniert nicht richtig.", "The keyboard does not work properly.", "لوحة المفاتيح لا تعمل بشكل صحيح.", 4),
    ("Ich mache ein Backup meiner Dateien.", "I make a backup of my files.", "أنا أعمل نسخة احتياطية لملفاتي.", 4),
]

for t in tech_a2:
    a2_sentences.append(f'    {{"german_text": "{t[0]}", "english_translation": "{t[1]}", "arabic_translation": "{t[2]}", "level": "A2", "difficulty_score": {t[3]}, "category": "Technology"}},')

# Social Media A2 (25)
social_a2 = [
    ("Ich habe ein Profil auf Facebook.", "I have a profile on Facebook.", "لدي بروفايل على فيسبوك.", 3),
    ("Ich poste jeden Tag etwas auf Instagram.", "I post something on Instagram every day.", "أنا أنشر شيئًا على إنستغرام كل يوم.", 4),
    ("Ich folge vielen Influencern auf TikTok.", "I follow many influencers on TikTok.", "أنا أتابع الكثير من المؤثرين على تيك توك.", 4),
    ("Ich kommentiere die Beiträge meiner Freunde.", "I comment on my friends' posts.", "أنا أعلق على منشورات أصدقائي.", 4),
    ("Ich teile interessante Artikel in meiner Story.", "I share interesting articles in my story.", "أنا أشارك مقالات مثيرة للاهتمام في قصتي.", 4),
    ("Ich lade Fotos von meiner Reise hoch.", "I upload photos from my trip.", "أنا أرفع صورًا من رحلتي.", 3),
    ("Ich bin in mehreren Gruppen auf Facebook.", "I am in several groups on Facebook.", "أنا في عدة مجموعات على فيسبوك.", 4),
    ("Ich verwalte die Social-Media-Kanäle meiner Firma.", "I manage the social media channels of my company.", "أنا أدير قنوات وسائل التواصل لشركتي.", 5),
    ("Ich schaue Live-Streams auf Twitch.", "I watch live streams on Twitch.", "أنا أشاهد البثوث المباشرة على تويتش.", 4),
    ("Ich benutze einen Hashtag für meine Posts.", "I use a hashtag for my posts.", "أنا أستخدم هاشتاق لمنشوراتي.", 4),
    ("Ich blockiere unbekannte Nutzer.", "I block unknown users.", "أنا أحظر المستخدمين المجهولين.", 3),
    ("Ich checke mein Handy alle zehn Minuten.", "I check my cell phone every ten minutes.", "أنا أتحقق من هاتفي كل عشر دقائق.", 4),
    ("Ich like die Fotos meiner Freunde.", "I like my friends' photos.", "أنا أعجب بصور أصدقائي.", 3),
    ("Ich schreibe eine Direktnachricht an meinen Kollegen.", "I write a direct message to my colleague.", "أنا أكتب رسالة مباشرة لزميلي.", 4),
    ("Ich veröffentliche ein Video über meine Hobbys.", "I publish a video about my hobbies.", "أنا أنشر فيديو عن هواياتي.", 4),
    ("Ich lese die Kommentare unter dem Beitrag.", "I read the comments under the post.", "أنا أقرأ التعليقات تحت المنشور.", 4),
    ("Ich erstelle einen Account auf LinkedIn.", "I create an account on LinkedIn.", "أنا أنشئ حسابًا على لينكد إن.", 4),
    ("Ich benutze einen Filter für mein Selfie.", "I use a filter for my selfie.", "أنا أستخدم فلترًا لصورتي الذاتية.", 4),
    ("Ich abonniere einen YouTube-Kanal.", "I subscribe to a YouTube channel.", "أنا أشترك في قناة يوتيوب.", 3),
    ("Ich reagiere mit Emojis auf Nachrichten.", "I react with emojis to messages.", "أنا أتفاعل بإيموجي مع الرسائل.", 4),
    ("Ich lösche alte Fotos von meinem Handy.", "I delete old photos from my cell phone.", "أنا أحذف الصور القديمة من هاتفي.", 3),
    ("Ich ändere mein Passwort regelmäßig.", "I change my password regularly.", "أنا أغير كلمة المرور بانتظام.", 4),
    ("Ich schalte die Benachrichtigungen aus.", "I turn off the notifications.", "أنا أطفئ الإشعارات.", 3),
    ("Ich vernetze mich mit anderen Profis.", "I network with other professionals.", "أنا أتواصل مع المحترفين الآخرين.", 5),
    ("Ich teile ein Event in meiner Story.", "I share an event in my story.", "أنا أشارك حدثًا في قصتي.", 4),
]

for s in social_a2:
    a2_sentences.append(f'    {{"german_text": "{s[0]}", "english_translation": "{s[1]}", "arabic_translation": "{s[2]}", "level": "A2", "difficulty_score": {s[3]}, "category": "Social Media"}},')

# Culture A2 (25)
culture_a2 = [
    ("Ich feiere Weihnachten mit meiner Familie.", "I celebrate Christmas with my family.", "أنا أحتفل بعيد الميلاد مع عائلتي.", 3),
    ("Der Karneval in Köln ist sehr berühmt.", "The carnival in Cologne is very famous.", "الكرنفال في كولن مشهور جدًا.", 4),
    ("Ich gehe ins Museum am Wochenende.", "I go to the museum on weekends.", "أنا أذهب للمتحف في عطلات نهاية الأسبوع.", 3),
    ("Die Berliner Mauer fiel 1989.", "The Berlin Wall fell in 1989.", "جدار برلين سقط في 1989.", 4),
    ("Ich trinke ein Bier im Biergarten.", "I drink a beer in the beer garden.", "أنا أشرب بيرة في حديقة البيرة.", 3),
    ("Der Oktoberfest findet in München statt.", "The Oktoberfest takes place in Munich.", "مهرجان أكتوبر يقام في ميونخ.", 4),
    ("Ich höre klassische Musik von Beethoven.", "I listen to classical music by Beethoven.", "أنا أستمع للموسيقى الكلاسيكية لبيتهوفن.", 4),
    ("Ich koche ein traditionelles deutsches Essen.", "I cook a traditional German meal.", "أنا أطبخ وجبة ألمانية تقليدية.", 4),
    ("Ich lese ein Buch über die deutsche Geschichte.", "I read a book about German history.", "أنا أقرأ كتابًا عن التاريخ الألماني.", 4),
    ("Die Oper in Wien ist weltberühmt.", "The opera in Vienna is world-famous.", "دار الأوبرا في فيينا مشهورة عالميًا.", 5),
    ("Ich gehe ins Theater am Freitag.", "I go to the theater on Friday.", "أنا أذهب للمسرح يوم الجمعة.", 3),
    ("Ich lerne die deutsche Kultur kennen.", "I get to know the German culture.", "أنا أتعرف على الثقافة الألمانية.", 4),
    ("Das Brandenburger Tor ist ein Wahrzeichen.", "The Brandenburg Gate is a landmark.", "بوابة براندنبورغ معلم سياحي.", 4),
    ("Ich singe im Chor meiner Stadt.", "I sing in the choir of my city.", "أنا أغني في جوقة مدينتي.", 3),
    ("Ich besuche die Burg Hohenzollern.", "I visit Hohenzollern Castle.", "أنا أزور قلعة هوهنزولرن.", 4),
    ("Ich probiere verschiedene deutsche Biere.", "I try various German beers.", "أنا أجرب أنواعًا مختلفة من البيرة الألمانية.", 4),
    ("Ich feiere den Tag der Deutschen Einheit.", "I celebrate German Unity Day.", "أنا أحتفل بيوم الوحدة الألمانية.", 4),
    ("Ich gehe zum Straßenfest in meinem Viertel.", "I go to the street festival in my neighborhood.", "أنا أذهب لمهرجان الشارع في حيي.", 4),
    ("Ich besuche ein Konzert von deutschen Künstlern.", "I visit a concert by German artists.", "أنا أزور حفلة لمطربين ألمان.", 4),
    ("Ich lerne traditionelle deutsche Tänze.", "I learn traditional German dances.", "أنا أتعلم الرقصات الألمانية التقليدية.", 4),
    ("Ich kaufe Souvenirs aus der Altstadt.", "I buy souvenirs from the old town.", "أنا أشتري تذكارات من المدينة القديمة.", 4),
    ("Ich trinke Glühwein auf dem Weihnachtsmarkt.", "I drink mulled wine at the Christmas market.", "أنا أشرب نبيذ التوابل في سوق عيد الميلاد.", 4),
    ("Ich schaue mir das Feuerwerk zum Silvester an.", "I watch the fireworks for New Year's Eve.", "أنا أشاهد الألعاب النارية لرأس السنة.", 4),
    ("Ich lese die Gedichte von Goethe.", "I read Goethe's poems.", "أنا أقرأ قصائد غوته.", 4),
    ("Ich besuche die Documenta in Kassel.", "I visit the Documenta in Kassel.", "أنا أزور الدوكومنتا في كاسل.", 5),
]

for c in culture_a2:
    a2_sentences.append(f'    {{"german_text": "{c[0]}", "english_translation": "{c[1]}", "arabic_translation": "{c[2]}", "level": "A2", "difficulty_score": {c[3]}, "category": "Culture"}},')

# Environment A2 (25)
environment_a2 = [
    ("Ich trenne den Müll in verschiedene Tonnen.", "I separate trash into different bins.", "أنا أفرز النفايات في سلال مختلفة.", 4),
    ("Ich fahre mit dem Fahrrad zur Arbeit.", "I ride my bike to work.", "أنا أقود دراجتي إلى العمل.", 3),
    ("Ich benutze eine wiederverwendbare Wasserflasche.", "I use a reusable water bottle.", "أنا أستخدم قنينة ماء قابلة لإعادة الاستخدام.", 4),
    ("Ich schalte das Licht aus, wenn ich den Raum verlasse.", "I turn off the light when I leave the room.", "أنا أطفئ النور عندما أغادر الغرفة.", 4),
    ("Ich kaufe keine Produkte mit Mikroplastik.", "I don't buy products with microplastics.", "أنا لا أشتري منتجات تحتوي على الميكروپلاستيك.", 5),
    ("Ich pflanze einen Baum im Garten.", "I plant a tree in the garden.", "أنا أزرع شجرة في الحديقة.", 3),
    ("Ich nutze öffentliche Verkehrsmittel.", "I use public transportation.", "أنا أستخدم وسائل النقل العامة.", 4),
    ("Ich reduziere meinen Fleischkonsum.", "I reduce my meat consumption.", "أنا أقلل استهلاكي للحوم.", 4),
    ("Ich nutze Solarenergie für mein Haus.", "I use solar energy for my house.", "أنا أستخدم الطاقة الشمسية لمنزلي.", 4),
    ("Ich kaufe lokale Produkte auf dem Markt.", "I buy local products at the market.", "أنا أشتري المنتجات المحلية في السوق.", 4),
    ("Ich verwende weniger Plastiktüten.", "I use fewer plastic bags.", "أنا أستخدم أكياس بلاستيكية أقل.", 4),
    ("Ich repariere meine Sachen statt sie wegzuwerfen.", "I repair my things instead of throwing them away.", "أنا أصلح أشيائي بدلًا من رميها.", 5),
    ("Ich kompostiere organische Abfälle.", "I compost organic waste.", "أنا أعمل كومپوست للمخلفات العضوية.", 4),
    ("Ich dusche kürzer, um Wasser zu sparen.", "I shower shorter to save water.", "أنا أستحم لمدة أقصر لتوفير الماء.", 4),
    ("Ich nutze ein E-Auto für die Umwelt.", "I use an electric car for the environment.", "أنا أستخدم سيارة كهربائية من أجل البيئة.", 5),
    ("Ich unterschreibe eine Petition für den Klimaschutz.", "I sign a petition for climate protection.", "أنا أوقع على عريضة لحماية المناخ.", 5),
    ("Ich kaufe Kleidung aus recycelten Materialien.", "I buy clothing from recycled materials.", "أنا أشتري ملابس من مواد معاد تدويرها.", 5),
    ("Ich vermeide Fast Fashion und kaufe qualitativ hochwertige Kleidung.", "I avoid fast fashion and buy high-quality clothing.", "أنا أتجنب الموضة السريعة وأشتري ملابس عالية الجودة.", 5),
    ("Ich pflanze ein Gemüsegarten auf meinem Balkon.", "I plant a vegetable garden on my balcony.", "أنا أزرع حديقة خضروات على شرفتي.", 4),
    ("Ich nehme meine eigene Tasse zum Kaffee mit.", "I take my own cup for coffee with me.", "أنا آخذ فنجاني الخاص للقهوة معي.", 4),
    ("Ich unterstütze Organisationen für den Naturschutz.", "I support organizations for nature conservation.", "أنا أدعم المنظمات لحماية الطبيعة.", 5),
    ("Ich verwende keine Einwegprodukte.", "I don't use disposable products.", "أنا لا أستخدم المنتجات ذات الاستخدام الواحد.", 4),
    ("Ich informiere mich über erneuerbare Energien.", "I inform myself about renewable energies.", "أنا أطلع على الطاقات المتجددة.", 5),
    ("Ich züchte meinen eigenen Gemüse im Garten.", "I grow my own vegetables in the garden.", "أنا أزرع خضرواتي الخاصة في الحديقة.", 4),
    ("Ich vermeide Lebensmittelverschwendung.", "I avoid food waste.", "أنا أتجنب هدر الطعام.", 4),
]

for e in environment_a2:
    a2_sentences.append(f'    {{"german_text": "{e[0]}", "english_translation": "{e[1]}", "arabic_translation": "{e[2]}", "level": "A2", "difficulty_score": {e[3]}, "category": "Environment"}},')

# Politics A2 (25)
politics_a2 = [
    ("Ich wähle bei der Bundestagswahl.", "I vote in the federal election.", "أنا أصوت في الانتخابات الفيدرالية.", 4),
    ("Die Politiker diskutieren im Parlament.", "The politicians discuss in parliament.", "السياسيون يناقشون في البرلمان.", 4),
    ("Ich interessiere mich für aktuelle Nachrichten.", "I am interested in current news.", "أنا مهتم بالأخبار الحالية.", 4),
    ("Die Demonstranten fordern Klimaschutz.", "The demonstrators demand climate protection.", "المتظاهرون يطالبون بحماية المناخ.", 5),
    ("Ich unterschreibe ein Petition für mehr Bildung.", "I sign a petition for more education.", "أنا أوقع على عريضة لمزيد من التعليم.", 5),
    ("Die Regierung beschließt neue Gesetze.", "The government decides on new laws.", "الحكومة تقرر قوانين جديدة.", 4),
    ("Ich schaue die Tagesschau im Fernsehen.", "I watch the daily news on TV.", "أنا أشاهد نشرة الأخبار اليومية في التلفاز.", 4),
    ("Die Parteien werben um Wählerstimmen.", "The parties campaign for voter votes.", "الأحزاب تستميل أصوات الناخبين.", 5),
    ("Ich diskutiere mit Freunden über Politik.", "I discuss politics with friends.", "أنا أناقش السياسة مع الأصدقاء.", 4),
    ("Die Koalition regiert mit Mehrheit.", "The coalition governs with a majority.", "الائتلاف يحكم بأغلبية.", 4),
    ("Ich lese Artikel in der Zeitung über Politik.", "I read articles in the newspaper about politics.", "أنا أقرأ مقالات في الجريدة عن السياسة.", 4),
    ("Die Opposition kritisiert die Regierung.", "The opposition criticizes the government.", "المعارضة تنتقد الحكومة.", 4),
    ("Ich engagiere mich ehrenamtlich in einem Verein.", "I volunteer in an association.", "أنا أتطوع في جمعية.", 4),
    ("Die Wahlen finden alle vier Jahre statt.", "The elections take place every four years.", "الانتخابات تقام كل أربع سنوات.", 4),
    ("Ich halte eine Rede vor dem Publikum.", "I give a speech in front of the audience.", "أنا ألقي خطابًا أمام الجمهور.", 4),
    ("Die Bürger protestieren gegen die Steuererhöhung.", "The citizens protest against the tax increase.", "المواطنون يحتجون ضد زيادة الضرائب.", 5),
    ("Ich schreibe einen Brief an den Abgeordneten.", "I write a letter to the representative.", "أنا أكتب رسالة إلى النائب.", 4),
    ("Die Pressefreiheit ist sehr wichtig.", "The press freedom is very important.", "حرية الصحافة مهمة جدًا.", 4),
    ("Ich nehme an einer Demonstration teil.", "I participate in a demonstration.", "أنا أشارك في مظاهرة.", 4),
    ("Die EU beschließt neue Regeln für alle Mitgliedsstaaten.", "The EU decides new rules for all member states.", "الاتحاد الأوروبي يقرر قواعد جديدة لكل الدول الأعضاء.", 5),
    ("Ich informiere mich über politische Parteien.", "I inform myself about political parties.", "أنا أطلع على الأحزاب السياسية.", 4),
    ("Die Kanzlerin besucht ein anderes Land.", "The chancellor visits another country.", "المستشارة تزور بلدًا آخر.", 4),
    ("Ich diskutiere über Menschenrechte.", "I discuss human rights.", "أنا أناقش حقوق الإنسان.", 4),
    ("Die Verfassung schützt die Grundrechte.", "The constitution protects fundamental rights.", "الدستور يحمي الحقوق الأساسية.", 4),
    ("Ich interessiere mich für internationale Beziehungen.", "I am interested in international relations.", "أنا مهتم بالعلاقات الدولية.", 5),
]

for p in politics_a2:
    a2_sentences.append(f'    {{"german_text": "{p[0]}", "english_translation": "{p[1]}", "arabic_translation": "{p[2]}", "level": "A2", "difficulty_score": {p[3]}, "category": "Politics"}},')

# Science A2 (25)
science_a2 = [
    ("Ich interessiere mich für Astronomie.", "I am interested in astronomy.", "أنا مهتم بعلم الفلك.", 4),
    ("Der Wissenschaftler erforscht das Weltall.", "The scientist explores outer space.", "العالم يستكشف الفضاء الخارجي.", 5),
    ("Ich lese Artikel über neue Technologien.", "I read articles about new technologies.", "أنا أقرأ مقالات عن التقنيات الجديدة.", 4),
    ("Die Evolutionstheorie erklärt die Entwicklung der Arten.", "The theory of evolution explains the development of species.", "نظرية التطور تفسر تطور الأنواع.", 5),
    ("Ich besuche ein Planetarium in der Stadt.", "I visit a planetarium in the city.", "أنا أزور قبة سماوية في المدينة.", 4),
    ("Die Forscher haben ein neues Medikament entdeckt.", "The researchers discovered a new medication.", "الباحثون اكتشفوا دواءً جديدًا.", 5),
    ("Ich lerne die chemischen Elemente auswendig.", "I memorize the chemical elements.", "أنا أحفظ العناصر الكيميائية.", 4),
    ("Der Roboter hilft im Haushalt.", "The robot helps with housework.", "الروبوت يساعد في أعمال المنزل.", 4),
    ("Ich schaue Dokumentationen über Tiere.", "I watch documentaries about animals.", "أنا أشاهد وثائقيات عن الحيوانات.", 4),
    ("Die Wissenschaft macht große Fortschritte.", "Science is making great progress.", "العلم يحقق تقدمًا كبيرًا.", 4),
    ("Ich probiere ein Experiment im Labor aus.", "I try out an experiment in the lab.", "أنا أجرب تجربة في المختبر.", 4),
    ("Der Computer simuliert komplexe Prozesse.", "The computer simulates complex processes.", "الكمبيوتر يحاكي العمليات المعقدة.", 5),
    ("Ich interessiere mich für Genetik.", "I am interested in genetics.", "أنا مهتم بالوراثيات.", 4),
    ("Die Sonne ist ein Stern im Universum.", "The sun is a star in the universe.", "الشمس هي نجم في الكون.", 3),
    ("Ich lerne die Planeten unseres Sonnensystems.", "I learn the planets of our solar system.", "أنا أتعلم كواكب مجموعتنا الشمسية.", 4),
    ("Die Bienen sind wichtig für die Bestäubung.", "The bees are important for pollination.", "النحل مهم للتلقيح.", 4),
    ("Ich lese über die Relativitätstheorie.", "I read about the theory of relativity.", "أنا أقرأ عن نظرية النسبية.", 5),
    ("Der Klimawandel betrifft uns alle.", "Climate change affects us all.", "تغير المناخ يؤثر علينا جميعًا.", 4),
    ("Ich besuche ein Science-Center mit meiner Klasse.", "I visit a science center with my class.", "أنا أزور مركز علوم مع صفي.", 4),
    ("Die DNA enthält die Erbinformationen.", "The DNA contains the genetic information.", "الـ DNA يحتوي على المعلومات الوراثية.", 5),
    ("Ich baue ein Modell des menschlichen Körpers.", "I build a model of the human body.", "أنا أبني نموذجًا للجسم البشري.", 4),
    ("Die Wissenschaftler publizieren ihre Ergebnisse.", "The scientists publish their results.", "العلماء ينشرون نتائجهم.", 4),
    ("Ich lerne über erneuerbare Energiequellen.", "I learn about renewable energy sources.", "أنا أتعلم عن مصادر الطاقة المتجددة.", 5),
    ("Der Laser wird in der Medizin eingesetzt.", "The laser is used in medicine.", "الليزر يستخدم في الطب.", 4),
    ("Ich besuche eine Vorlesung an der Universität.", "I attend a lecture at the university.", "أنا أحضر محاضرة في الجامعة.", 4),
]

for s in science_a2:
    a2_sentences.append(f'    {{"german_text": "{s[0]}", "english_translation": "{s[1]}", "arabic_translation": "{s[2]}", "level": "A2", "difficulty_score": {s[3]}, "category": "Science"}},')

# Philosophy A2 (25)
philosophy_a2 = [
    ("Ich denke über den Sinn des Lebens nach.", "I think about the meaning of life.", "أنا أفكر في معنى الحياة.", 4),
    ("Was ist richtig und was ist falsch?", "What is right and what is wrong?", "ما هو صحيح وما هو خاطئ؟", 3),
    ("Ich philosophiere mit meinen Freunden.", "I philosophize with my friends.", "أنا أتفلسف مع أصدقائي.", 4),
    ("Die Wahrheit ist manchmal schwer zu finden.", "The truth is sometimes hard to find.", "الحقيقة أحيانًا يصعب العثور عليها.", 4),
    ("Ich hinterfrage die gesellschaftlichen Normen.", "I question societal norms.", "أنا أتسائل المعايير المجتمعية.", 5),
    ("Was ist Glück für mich?", "What is happiness for me?", "ما هو السعادة بالنسبة لي؟", 3),
    ("Ich lese philosophische Texte von Kant.", "I read philosophical texts by Kant.", "أنا أقرأ نصوص فلسفية لكانت.", 5),
    ("Die Freiheit ist ein hohes Gut.", "Freedom is a high value.", "الحرية قيمة عليا.", 4),
    ("Ich diskutiere über Ethik und Moral.", "I discuss ethics and morals.", "أنا أناقش الأخلاق والسلوك.", 4),
    ("Was ist der Sinn der Existenz?", "What is the meaning of existence?", "ما هو معنى الوجود؟", 4),
    ("Ich reflektiere über meine Entscheidungen.", "I reflect on my decisions.", "أنا أتأمل في قراراتي.", 4),
    ("Die Zeit vergeht und wir werden älter.", "Time passes and we get older.", "الوقت يمر ونحن نكبر في السن.", 3),
    ("Ich hinterfrage meine eigenen Überzeugungen.", "I question my own beliefs.", "أنا أتسائل معتقداتي الخاصة.", 4),
    ("Was ist wirklich wichtig im Leben?", "What is really important in life?", "ما هو مهم حقًا في الحياة؟", 4),
    ("Ich lerne stoische Philosophie kennen.", "I get to know Stoic philosophy.", "أنا أتعرف على الفلسفة الرواقية.", 5),
    ("Die Gerechtigkeit sollte für alle gelten.", "Justice should apply to everyone.", "العدالة يجب أن تنطبق على الجميع.", 4),
    ("Ich denke über den Tod nach.", "I think about death.", "أنا أفكر في الموت.", 3),
    ("Was macht den Menschen aus?", "What makes a human being?", "ما الذي يصنع الإنسان؟", 4),
    ("Ich diskutiere über Determinismus und Freiheit.", "I discuss determinism and freedom.", "أنا أناقش الحتمية والحرية.", 5),
    ("Die Vernunft unterscheidet den Menschen vom Tier.", "Reason distinguishes man from animal.", "العقل يميز الإنسان عن الحيوان.", 4),
    ("Ich philosophiere über die Zukunft der Menschheit.", "I philosophize about the future of mankind.", "أنا أتفلسف عن مستقبل البشرية.", 5),
    ("Was ist das Wesen der Liebe?", "What is the essence of love?", "ما هو جوهر الحب؟", 4),
    ("Ich lese Sartre und Camus.", "I read Sartre and Camus.", "أنا أقرأ سارتر وكامو.", 4),
    ("Die Wahrheit liegt manchmal in der Mitte.", "Truth sometimes lies in the middle.", "الحقيقة أحيانًا تكمن في الوسط.", 4),
    ("Ich versuche ein authentisches Leben zu führen.", "I try to lead an authentic life.", "أنا أحاول قيادة حياة أصيلة.", 5),
]

for p in philosophy_a2:
    a2_sentences.append(f'    {{"german_text": "{p[0]}", "english_translation": "{p[1]}", "arabic_translation": "{p[2]}", "level": "A2", "difficulty_score": {p[3]}, "category": "Philosophy"}},')

# Business A2 (25)
business_a2 = [
    ("Ich gründe ein Unternehmen mit zwei Partnern.", "I found a company with two partners.", "أنا أؤسس شركة مع شريكين.", 5),
    ("Der Geschäftsbericht zeigt Gewinn für dieses Jahr.", "The business report shows profit for this year.", "تقرير الأعمال يظهر ربحًا لهذا العام.", 5),
    ("Ich verhandle mit Lieferanten über Preise.", "I negotiate with suppliers about prices.", "أنا أتفاوض مع الموردين حول الأسعار.", 5),
    ("Die Firma expandiert auf den asiatischen Markt.", "The company expands to the Asian market.", "الشركة تتوسع إلى السوق الآسيوي.", 5),
    ("Ich erstelle ein Marketingkonzept für unser Produkt.", "I create a marketing concept for our product.", "أنا أضع مفهوم تسويقي لمنتجنا.", 5),
    ("Der Verkaufszahlen sind dieses Quartal gestiegen.", "The sales figures rose this quarter.", "أرقام المبيعات ارتفعت هذا الربع.", 5),
    ("Ich führe ein Vorstellungsgespräch mit Bewerbern.", "I conduct job interviews with applicants.", "أنا أجري مقابلات عمل مع المتقدمين.", 5),
    ("Die Aktienkurse fallen heute stark.", "The stock prices fall sharply today.", "أسعار الأسهم تهبط بقوة اليوم.", 5),
    ("Ich erstelle eine Budgetplanung für nächstes Jahr.", "I create a budget plan for next year.", "أنا أضع خطة ميزانية للعام القادم.", 5),
    ("Die Konkurrenz bietet ähnliche Produkte an.", "The competition offers similar products.", "المنافسة تقدم منتجات مشابهة.", 4),
    ("Ich analysiere den Markt für unsere Strategie.", "I analyze the market for our strategy.", "أنا أحلل السوق لاستراتيجيتنا.", 5),
    ("Der Kunde beschwert sich über die Qualität.", "The customer complains about the quality.", "العميل يشتكي من الجودة.", 4),
    ("Ich schließe einen Vertrag mit dem neuen Kunden.", "I close a contract with the new customer.", "أنا أغلق عقدًا مع العميل الجديد.", 5),
    ("Die Firma investiert in Forschung und Entwicklung.", "The company invests in research and development.", "الشركة تستثمر في البحث والتطوير.", 5),
    ("Ich präsentiere die Ergebnisse dem Vorstand.", "I present the results to the board.", "أنا أعرض النتائج لمجلس الإدارة.", 5),
    ("Die Bilanz sieht für dieses Jahr sehr gut aus.", "The balance sheet looks very good for this year.", "الميزانية تبدو جيدة جدًا لهذا العام.", 5),
    ("Ich besuche eine Handelsmesse in Frankfurt.", "I visit a trade fair in Frankfurt.", "أنا أزور معرض تجاري في فرانكفورت.", 4),
    ("Die Mitarbeiterzufriedenheit ist sehr wichtig.", "Employee satisfaction is very important.", "رضا الموظفين مهم جدًا.", 4),
    ("Ich entwickle eine neue Strategie für das Unternehmen.", "I develop a new strategy for the company.", "أنا أطور استراتيجية جديدة للشركة.", 5),
    ("Die Firma fusioniert mit einem Konkurrenten.", "The company merges with a competitor.", "الشركة تندمج مع منافس.", 5),
    ("Ich optimiere die Arbeitsprozesse in der Abteilung.", "I optimize work processes in the department.", "أنا أحسن عمليات العمل في القسم.", 5),
    ("Der Umsatz ist im Vergleich zum Vorjahr gestiegen.", "The revenue increased compared to last year.", "الإيرادات ارتفعت مقارنة بالعام الماضي.", 5),
    ("Ich plane die Expansion in neue Märkte.", "I plan the expansion to new markets.", "أنا أخطط للتوسع إلى أسواق جديدة.", 5),
    ("Die Firma gewinnt einen wichtigen Auftrag.", "The company wins an important contract.", "الشركة تفوز بعقد مهم.", 5),
    ("Ich bewerte die Leistung meiner Abteilung.", "I evaluate the performance of my department.", "أنا أقيم أداء قسمي.", 5),
]

for b in business_a2:
    a2_sentences.append(f'    {{"german_text": "{b[0]}", "english_translation": "{b[1]}", "arabic_translation": "{b[2]}", "level": "A2", "difficulty_score": {b[3]}, "category": "Business"}},')

print(f"A2 sentences prepared: {len(a2_sentences)}")

# Now write the actual file
output_lines = []
output_lines.append('from app.core.database import SessionLocal, engine, Base')
output_lines.append('from app.models import Sentence')
output_lines.append('import random')
output_lines.append('')
output_lines.append('Base.metadata.create_all(bind=engine)')
output_lines.append('')
output_lines.append('# Check existing sentence count')
output_lines.append('session = SessionLocal()')
output_lines.append('try:')
output_lines.append('    existing_count = session.query(Sentence).count()')
output_lines.append('    if existing_count > 50:')
output_lines.append('        print(f"Database already has {existing_count} sentences (>50), skipping seed.")')
output_lines.append('        session.close()')
output_lines.append('        exit()')
output_lines.append('finally:')
output_lines.append('    session.close()')
output_lines.append('')
output_lines.append('# All 2000 sentences')
output_lines.append('sentences = [')
output_lines.append('# ==================== A1 (300 sentences, difficulty 1-3) ====================')

for s in a1_sentences:
    output_lines.append(s)

output_lines.append('# ==================== A2 (400 sentences, difficulty 2-4) ====================')

for s in a2_sentences:
    output_lines.append(s)

output_lines.append(']')
output_lines.append('')
output_lines.append('# Insert in batches of 100')
output_lines.append('session = SessionLocal()')
output_lines.append('try:')
output_lines.append('    for i in range(0, len(sentences), 100):')
output_lines.append('        batch = sentences[i:i+100]')
output_lines.append('        sentence_objects = [Sentence(**s) for s in batch]')
output_lines.append('        session.bulk_save_objects(sentence_objects)')
output_lines.append('        session.commit()')
output_lines.append('        print(f"Inserted {min(i+100, len(sentences))}/{len(sentences)} sentences...")')
output_lines.append('    print(f"Successfully seeded {len(sentences)} sentences!")')
output_lines.append('except Exception as e:')
output_lines.append('    session.rollback()')
output_lines.append('    print(f"Error: {e}")')
output_lines.append('    raise')
output_lines.append('finally:')
output_lines.append('    session.close()')

# Write to file
with open('seed_all_sentences.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print(f"File seed_all_sentences.py created with {len(a1_sentences) + len(a2_sentences)} sentences")
print(f"Total lines written: {len(output_lines)}")
