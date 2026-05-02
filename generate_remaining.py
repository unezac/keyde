import json

# This script generates B1, B2, C1 sentences (1300 total)
# to complete the 2000 sentence seed file

all_sentences = []

# ==================== B1 (500 sentences, difficulty 3-5) ====================

# Work B1 (50 sentences)
work_b1 = [
    ("Obwohl ich müde bin, arbeite ich weiter an dem Projekt.", "Although I am tired, I continue working on the project.", "على الرغم من تعبي، أستمر في العمل على المشروع.", 4, "Work"),
    ("Nachdem ich die Präsentation vorbereitet hatte, übte ich meinen Vortrag.", "After I had prepared the presentation, I practiced my speech.", "بعد أن جهزت العرض التقديمي، تدربت على خطابي.", 5, "Work"),
    ("Während des Meetings wurden wichtige Entscheidungen getroffen.", "Important decisions were made during the meeting.", "خلال الاجتماع، تم اتخاذ قرارات مهمة.", 4, "Work"),
    ("Da ich krank bin, kann ich heute nicht zur Arbeit kommen.", "Since I am sick, I cannot come to work today.", "بما أنني مريض، لا يمكنني الحضور للعمل اليوم.", 4, "Work"),
    ("Bevor wir das Projekt starten, müssen wir den Zeitplan festlegen.", "Before we start the project, we must set the schedule.", "قبل أن نبدأ المشروع، يجب أن نحدد الجدول الزمني.", 5, "Work"),
    ("Ich habe gelernt, dass Teamarbeit sehr wichtig ist.", "I have learned that teamwork is very important.", "لقد تعلمت أن العمل الجماعي مهم جدًا.", 4, "Work"),
    ("Wenn ich mehr Zeit hätte, würde ich ein eigenes Unternehmen gründen.", "If I had more time, I would found my own company.", "لو كان لدي وقت أكثر، سأؤسس شركتي الخاصة.", 5, "Work"),
    ("Seitdem ich in dieser Firma arbeite, habe ich viel gelernt.", "Since I have been working in this company, I have learned a lot.", "منذ أن أعمل في هذه الشركة، تعلمت الكثير.", 5, "Work"),
    ("Dass er die Beförderung bekommen hat, freut mich sehr.", "That he got the promotion makes me very happy.", "أنه حصل على الترقية يسعدني كثيرًا.", 5, "Work"),
    ("Ich bereue es, nicht früher mit dem Studium begonnen zu haben.", "I regret not starting my studies earlier.", "أنا ندم على عدم بدء دراستي في وقت أبكر.", 5, "Work"),
    ("Die Kollegen, mit denen ich zusammenarbeite, sind sehr kompetent.", "The colleagues I work with are very competent.", "الزملاء الذين أعمل معهم أكفاء جدًا.", 5, "Work"),
    ("Es ist mir gelungen, den Kunden zu überzeugen.", "I succeeded in convincing the customer.", "لقد نجحت في إقناع العميل.", 4, "Work"),
    ("Ich plane, nächstes Jahr eine Fortbildung zu machen.", "I plan to do further training next year.", "أنا أخطط للقيام بتدريب إضافي العام القادم.", 5, "Work"),
    ("Solange ich gesund bin, werde ich Vollzeit arbeiten.", "As long as I am healthy, I will work full-time.", "طالما أنا بصحة جيدة، سأعمل بدوام كامل.", 5, "Work"),
    ("Ich habe vor, meine Karriere in Richtung Management zu lenken.", "I intend to steer my career towards management.", "أنا أنوي توجيه مسيرتي المهنية نحو الإدارة.", 5, "Work"),
    ("Durch die Zusammenarbeit mit Experten habe ich viel gelernt.", "Through collaboration with experts, I have learned a lot.", "من خلال التعاون مع الخبراء، تعلمت الكثير.", 5, "Work"),
    ("Obwohl der Stress hoch ist, genieße ich meinen Job.", "Although the stress is high, I enjoy my job.", "على الرغم من التوتر العالي، أستمتع بعملي.", 5, "Work"),
    ("Ich habe die Möglichkeit, im Ausland zu arbeiten.", "I have the opportunity to work abroad.", "لدي فرصة للعمل في الخارج.", 4, "Work"),
    ("Es wäre besser, wenn wir mehr kommunizieren würden.", "It would be better if we communicated more.", "سيكون من الأفضل لو تواصلنا أكثر.", 5, "Work"),
    ("Nach der Arbeit gehe ich oft ins Fitnessstudio.", "After work, I often go to the fitness studio.", "بعد العمل، أذهب غالبًا للنادي الرياضي.", 4, "Work"),
    ("Ich bin dafür verantwortlich, das Budget zu verwalten.", "I am responsible for managing the budget.", "أنا مسؤول عن إدارة الميزانية.", 5, "Work"),
    ("Die Firma bietet flexible Arbeitszeiten an.", "The company offers flexible working hours.", "الشركة تقدم ساعات عمل مرنة.", 4, "Work"),
    ("Ich habe eine Deadline bis nächsten Freitag.", "I have a deadline until next Friday.", "لدي موعد نهائي حتى الجمعة القادمة.", 4, "Work"),
    ("Wir müssen die Qualität unserer Produkte verbessern.", "We must improve the quality of our products.", "يجب علينا تحسين جودة منتجاتنا.", 5, "Work"),
    ("Ich nehme an einer Konferenz über Digitalisierung teil.", "I participate in a conference about digitalization.", "أنا أشارك في مؤتمر حول الرقمنة.", 5, "Work"),
    ("Das Gehalt wird anhand der Leistung berechnet.", "The salary is calculated based on performance.", "الراتب يُحسب بناءً على الأداء.", 5, "Work"),
    ("Ich habe einen Termin beim Steuerberater.", "I have an appointment with the tax advisor.", "لدي موعد مع مستشار ضريبي.", 4, "Work"),
    ("Die Arbeitsbedingungen haben sich verbessert.", "The working conditions have improved.", "ظروف العمل تحسنت.", 4, "Work"),
    ("Ich bewerbe mich um eine Stelle als Projektmanager.", "I apply for a position as project manager.", "أنا أتقدم لوظيفة كمدير مشاريع.", 5, "Work"),
    ("Wir feiern das Jubiläum der Firma.", "We celebrate the anniversary of the company.", "نحتفل بالذكرى السنوية للشركة.", 4, "Work"),
    ("Der Betriebsrat vertritt die Interessen der Mitarbeiter.", "The works council represents the interests of employees.", "مجلس العمل يمثل مصالح الموظفين.", 5, "Work"),
    ("Ich habe eine Ausbildung als Kaufmann gemacht.", "I completed an apprenticeship as a merchant.", "لقد أكملت تدريبًا مهنيًا كتاجر.", 5, "Work"),
    ("Die Arbeitslosigkeit ist in dieser Region hoch.", "Unemployment is high in this region.", "البطالة مرتفعة في هذه المنطقة.", 4, "Work"),
    ("Ich arbeite als freiberuflicher Berater.", "I work as a freelance consultant.", "أنا أعمل كمستشار مستقل.", 5, "Work"),
    ("Die Firma hat ein neues Bürogebäude eröffnet.", "The company opened a new office building.", "الشركة افتتحت مبنى مكاتب جديد.", 4, "Work"),
    ("Ich nutze moderne Technologien im Beruf.", "I use modern technologies in my profession.", "أنا أستخدم تقنيات حديثة في مهنتي.", 5, "Work"),
    ("Die Work-Life-Balance ist mir sehr wichtig.", "Work-life balance is very important to me.", "التوازن بين العمل والحياة مهم جدًا بالنسبة لي.", 5, "Work"),
    ("Ich habe einen befristeten Arbeitsvertrag.", "I have a temporary employment contract.", "لدي عقد عمل مؤقت.", 4, "Work"),
    ("Die Gehaltsverhandlung war erfolgreich.", "The salary negotiation was successful.", "مفاوضات الراتب كانت ناجحة.", 5, "Work"),
    ("Ich arbeite in einem internationalen Team.", "I work in an international team.", "أنا أعمل في فريق دولي.", 4, "Work"),
    ("Der Chef hat die Prämie für gute Leistung gegeben.", "The boss gave the bonus for good performance.", "المدير أعطى المكافأة للأداء الجيد.", 5, "Work"),
    ("Ich habe eine Kündigungsfrist von drei Monaten.", "I have a notice period of three months.", "لدي فترة إشعار لمدة ثلاثة أشهر.", 5, "Work"),
    ("Wir führen ein Mitarbeitergespräch einmal im Monat.", "We conduct an employee meeting once a month.", "نحن نجري اجتماع موظفين مرة في الشهر.", 5, "Work"),
    ("Ich habe die Zertifizierung in Projektmanagement erhalten.", "I received the certification in project management.", "لقد حصلت على الشهادة في إدارة المشاريع.", 5, "Work"),
    ("Die Firma bietet Homeoffice an.", "The company offers home office.", "الشركة توفر العمل من المنزل.", 4, "Work"),
    ("Ich reise geschäftlich oft nach Berlin.", "I travel on business often to Berlin.", "أنا أسافر للعمل غالبًا إلى برلين.", 5, "Work"),
    ("Die Unternehmenskultur fördert Innovationen.", "The corporate culture promotes innovations.", "ثقافة الشركة تعزز الابتكارات.", 5, "Work"),
    ("Ich habe einen Mentor, der mich unterstützt.", "I have a mentor who supports me.", "لدي مرشد يدعمني.", 4, "Work"),
]

# Education B1 (50 sentences)
education_b1 = [
    ("Ich habe mich entschieden, ein Semester im Ausland zu studieren.", "I decided to study one semester abroad.", "لقد قررت الدراسة لفصل دراسي في الخارج.", 5, "Education"),
    ("Das Studium erfordert viel Disziplin und Eigeninitiative.", "The studies require a lot of discipline and initiative.", "الدراسة تتطلب الكثير من الانضباط والمبادرة.", 5, "Education"),
    ("Ich schreibe meine Bachelorarbeit über künstliche Intelligenz.", "I am writing my bachelor thesis about artificial intelligence.", "أنا أكتب أطروحتي الجامعية حول الذكاء الاصطناعي.", 5, "Education"),
    ("Die Vorlesung findet jeden Dienstag und Donnerstag statt.", "The lecture takes place every Tuesday and Thursday.", "المحاضرة تُعقد كل ثلاثاء وخميس.", 4, "Education"),
    ("Ich habe mich für drei Kurse eingeschrieben.", "I enrolled in three courses.", "لقد سجلت في ثلاثة مقررات.", 4, "Education"),
    ("Die Bibliothek ist bis 22 Uhr am Abend geöffnet.", "The library is open until 10 PM in the evening.", "المكتبة مفتوحة حتى الساعة 10 مساءً.", 4, "Education"),
    ("Ich nehme an einem Erasmus-Programm teil.", "I participate in an Erasmus program.", "أنا أشارك في برنامج إيراسموس.", 5, "Education"),
    ("Die Prüfungsvorbereitung dauert meistens mehrere Wochen.", "Exam preparation usually takes several weeks.", "التحضير للامتحان يستغرق عادة عدة أسابيع.", 5, "Education"),
    ("Ich wohne in einem Wohnheim mit anderen Studenten.", "I live in a dormitory with other students.", "أنا أعيش في سكن مع طلاب آخرين.", 4, "Education"),
    ("Der Professor hat eine interessante Forschungsarbeit veröffentlicht.", "The professor published an interesting research paper.", "الأستاذ نشر ورقة بحثية مثيرة للاهتمام.", 5, "Education"),
    ("Ich nutze Online-Plattformen für das Selbststudium.", "I use online platforms for self-study.", "أنا أستخدم المنصات الإلكترونية للدراسة الذاتية.", 5, "Education"),
    ("Die Note im Zeugnis ist sehr wichtig für die Zukunft.", "The grade on the certificate is very important for the future.", "الدرجة في الشهادة مهمة جدًا للمستقبل.", 5, "Education"),
    ("Ich habe ein Stipendium für hervorragende Leistungen bekommen.", "I received a scholarship for excellent performance.", "حصلت على منحة دراسية للأداء الممتاز.", 5, "Education"),
    ("Die Gruppenarbeit fördert die sozialen Kompetenzen.", "Group work promotes social skills.", "العمل الجماعي يعزز المهارات الاجتماعية.", 5, "Education"),
    ("Ich lerne effektiver, wenn ich mir Notizen mache.", "I learn more effectively when I take notes.", "أنا أتعلم بشكل أكثر فعالية عندما آخذ ملاحظات.", 5, "Education"),
    ("Der Semesterbeginn wird mit einer Party gefeiert.", "The start of the semester is celebrated with a party.", "بداية الفصل الدراسي تحتفل بحفلة.", 4, "Education"),
    ("Ich habe Prüfungsangst vor der mündlichen Prüfung.", "I have exam anxiety before the oral exam.", "لدي قلق من الامتحان قبل الامتحان الشفوي.", 4, "Education"),
    ("Die Universität bietet viele Sportkurse an.", "The university offers many sports courses.", "الجامعة تقدم العديد من دورات الرياضة.", 4, "Education"),
    ("Ich habe mich für ein Praktikum in einem Unternehmen beworben.", "I applied for an internship in a company.", "تقدمت لتدريب داخلي في شركة.", 5, "Education"),
    ("Das Studium der Medizin dauert mindestens sechs Jahre.", "Studying medicine takes at least six years.", "دراسة الطب تستغرق ست سنوات على الأقل.", 5, "Education"),
    ("Ich besuche ein Sprachkurs für Fortgeschrittene.", "I attend a language course for advanced learners.", "أنا أحضر دورة لغة للمتعلمين المتقدمين.", 5, "Education"),
    ("Die Hausarbeit muss eine bestimmte Seitenanzahl haben.", "The term paper must have a certain number of pages.", "الورقة الفصلية يجب أن يكون لها عدد معين من الصفحات.", 5, "Education"),
    ("Ich nutze die Sprechstunde des Professors.", "I use the professor's office hours.", "أنا أستخدم ساعات مكتب الأستاذ.", 4, "Education"),
    ("Die Studentenvertretung organisiert viele Events.", "The student council organizes many events.", "مجلس الطلاب ينظم العديد من الفعاليات.", 5, "Education"),
    ("Ich habe ein Auslandssemester in Spanien geplant.", "I planned a semester abroad in Spain.", "لقد خططت لفصل دراسي في الخارج في إسبانيا.", 5, "Education"),
    ("Die Lernplattform ist benutzerfreundlich gestaltet.", "The learning platform is designed user-friendly.", "منصة التعلم مصممة بطريقة سهلة الاستخدام.", 5, "Education"),
    ("Ich muss das Modul bis zum Ende des Semesters abschließen.", "I must complete the module by the end of the semester.", "يجب أن أتم الموديل بحلول نهاية الفصل الدراسي.", 5, "Education"),
    ("Die Bibliothek bietet auch E-Books zum Ausleihen an.", "The library also offers e-books for borrowing.", "المكتبة تقدم أيضًا كتبًا إلكترونية للإعارة.", 4, "Education"),
    ("Ich habe ein Forschungsprojekt über Klimawandel gestartet.", "I started a research project about climate change.", "لقد بدأت مشروع بحثي حول تغير المناخ.", 5, "Education"),
    ("Die Dozentin erklärt die komplexen Themen sehr anschaulich.", "The lecturer explains complex topics very vividly.", "المحاضرة تشرح الموضوعات المعقدة بشكل حيوي جدًا.", 5, "Education"),
    ("Ich habe die Zulassung für den Masterstudiengang erhalten.", "I received admission for the master's program.", "لقد حصلت على القبول لبرنامج الماجستير.", 5, "Education"),
    ("Das Studium finanziert sich durch einen Nebenjob.", "The studies are financed through a side job.", "الدراسة تمول من خلال وظيفة جانبية.", 5, "Education"),
    ("Ich besuche eine Vorlesung über Wirtschaftspolitik.", "I attend a lecture on economic policy.", "أنا أحضر محاضرة حول السياسة الاقتصادية.", 5, "Education"),
    ("Die Mensa bietet gesundes Essen zu günstigen Preisen.", "The cafeteria offers healthy food at reasonable prices.", "الكافيتريا تقدم طعامًا صحيًا بأسعار معقولة.", 4, "Education"),
    ("Ich habe eine Lernpause für eine Woche eingelegt.", "I took a study break for a week.", "لقد أخذت استراحة دراسية لمدة أسبوع.", 4, "Education"),
    ("Die Abschlussfeier findet in der Aula statt.", "The graduation ceremony takes place in the auditorium.", "حفل التخرج يُعقد في القاعة الكبرى.", 4, "Education"),
    ("Ich schreibe mir wichtige Informationen in ein Heft.", "I write important information in a notebook.", "أنا أكتب معلومات مهمة في دفتر.", 4, "Education"),
    ("Die Prüfungsordnung legt die Regeln fest.", "The examination regulations set the rules.", "لوائح الامتحانات تضع القواعد.", 5, "Education"),
    ("Ich habe einen Tutor, der mir bei Fragen hilft.", "I have a tutor who helps me with questions.", "لدي معلم خصوصي يساعدني في الأسئلة.", 4, "Education"),
    ("Die Fernuni bietet viele flexible Studiengänge an.", "The distance university offers many flexible study programs.", "الجامعة عن بعد تقدم العديد من برامج الدراسة المرنة.", 5, "Education"),
    ("Ich habe mich für ein Austauschprogramm beworben.", "I applied for an exchange program.", "تقدمت لبرنامج تبادل.", 5, "Education"),
    ("Das Studium generale bietet interdisziplinäre Kurse.", "General studies offer interdisciplinary courses.", "الدراسات العامة تقدم مقررات متعددة التخصصات.", 5, "Education"),
    ("Ich lerne mit Karteikarten Vokabeln.", "I learn vocabulary with flashcards.", "أنا أتعلم المفردات ببطاقات التعلم.", 4, "Education"),
    ("Die Semesterferien nutze ich für eine Reise.", "I use the semester break for a trip.", "أنا أستخدم عطلة الفصل الدراسي لرحلة.", 4, "Education"),
    ("Ich habe eine Gruppenarbeit über Geschichte vorbereitet.", "I prepared a group work about history.", "لقد أعددت عملًا جماعيًا حول التاريخ.", 5, "Education"),
    ("Die Vorlesung wurde aufgrund von Krankheit ausgefallen.", "The lecture was cancelled due to illness.", "المحاضرة أُلغيت بسبب المرض.", 4, "Education"),
    ("Ich habe ein Zertifikat in Datenanalyse erworben.", "I acquired a certificate in data analysis.", "لقد حصلت على شهادة في تحليل البيانات.", 5, "Education"),
]

# Add B1 sentences
for s in work_b1:
    all_sentences.append((s[0], s[1], s[2], "B1", s[3], s[4]))
for s in education_b1:
    all_sentences.append((s[0], s[1], s[2], "B1", s[3], s[4]))

print(f"B1 sentences so far: {len([s for s in all_sentences if s[3] == 'B1'])}")

# Continue with more B1 categories...
# (Due to length, I'll write the rest in parts)

print(f"Total B1 sentences to add: {len(all_sentences)}")
