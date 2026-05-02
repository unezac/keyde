#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add B1, B2, C1 sentences to seed_all_sentences.py
Run this after the existing seed_all_sentences.py is created
"""

# B1 sentences (500 total) - difficulty 3-5
b1_sentences = []

# B1 Work (50)
b1_work = [
    ("Obwohl ich müde bin, arbeite ich weiter an dem Projekt.", "Although I am tired, I continue working on the project.", "على الرغم من تعبي، أستمر في العمل على المشروع.", "B1", 4, "Work"),
    ("Nachdem ich die Präsentation vorbereitet hatte, übte ich meinen Vortrag.", "After I had prepared the presentation, I practiced my speech.", "بعد أن جهزت العرض التقديمي، تدربت على خطابي.", "B1", 5, "Work"),
    ("Während des Meetings wurden wichtige Entscheidungen getroffen.", "Important decisions were made during the meeting.", "خلال الاجتماع، تم اتخاذ قرارات مهمة.", "B1", 4, "Work"),
    ("Da ich krank bin, kann ich heute nicht zur Arbeit kommen.", "Since I am sick, I cannot come to work today.", "بما أنني مريض، لا يمكنني الحضور للعمل اليوم.", "B1", 4, "Work"),
    ("Bevor wir das Projekt starten, müssen wir den Zeitplan festlegen.", "Before we start the project, we must set the schedule.", "قبل أن نبدأ المشروع، يجب أن نحدد الجدول الزمني.", "B1", 5, "Work"),
    ("Ich habe gelernt, dass Teamarbeit sehr wichtig ist.", "I have learned that teamwork is very important.", "لقد تعلمت أن العمل الجماعي مهم جدًا.", "B1", 4, "Work"),
    ("Wenn ich mehr Zeit hätte, würde ich ein eigenes Unternehmen gründen.", "If I had more time, I would found my own company.", "لو كان لدي وقت أكثر، سأؤسس شركتي الخاصة.", "B1", 5, "Work"),
    ("Seitdem ich in dieser Firma arbeite, habe ich viel gelernt.", "Since I have been working in this company, I have learned a lot.", "منذ أن أعمل في هذه الشركة، تعلمت الكثير.", "B1", 5, "Work"),
    ("Dass er die Beförderung bekommen hat, freut mich sehr.", "That he got the promotion makes me very happy.", "أنه حصل على الترقية يسعدني كثيرًا.", "B1", 5, "Work"),
    ("Ich bereue es, nicht früher mit dem Studium begonnen zu haben.", "I regret not starting my studies earlier.", "أنا ندم على عدم بدء دراستي في وقت أبكر.", "B1", 5, "Work"),
    ("Die Kollegen, mit denen ich zusammenarbeite, sind sehr kompetent.", "The colleagues I work with are very competent.", "الزملاء الذين أعمل معهم أكفاء جدًا.", "B1", 5, "Work"),
    ("Es ist mir gelungen, den Kunden zu überzeugen.", "I succeeded in convincing the customer.", "لقد نجحت في إقناع العميل.", "B1", 4, "Work"),
    ("Ich plane, nächstes Jahr eine Fortbildung zu machen.", "I plan to do further training next year.", "أنا أخطط للقيام بتدريب إضافي العام القادم.", "B1", 5, "Work"),
    ("Solange ich gesund bin, werde ich Vollzeit arbeiten.", "As long as I am healthy, I will work full-time.", "طالما أنا بصحة جيدة، سأعمل بدوام كامل.", "B1", 5, "Work"),
    ("Ich habe vor, meine Karriere in Richtung Management zu lenken.", "I intend to steer my career towards management.", "أنا أنوي توجيه مسيرتي المهنية نحو الإدارة.", "B1", 5, "Work"),
    ("Durch die Zusammenarbeit mit Experten habe ich viel gelernt.", "Through collaboration with experts, I have learned a lot.", "من خلال التعاون مع الخبراء، تعلمت الكثير.", "B1", 5, "Work"),
    ("Obwohl der Stress hoch ist, genieße ich meinen Job.", "Although the stress is high, I enjoy my job.", "على الرغم من التوتر العالي، أستمتع بعملي.", "B1", 5, "Work"),
    ("Ich habe die Möglichkeit, im Ausland zu arbeiten.", "I have the opportunity to work abroad.", "لدي فرصة للعمل في الخارج.", "B1", 4, "Work"),
    ("Es wäre besser, wenn wir mehr kommunizieren würden.", "It would be better if we communicated more.", "سيكون من الأفضل لو تواصلنا أكثر.", "B1", 5, "Work"),
    ("Nach der Arbeit gehe ich oft ins Fitnessstudio.", "After work, I often go to the fitness studio.", "بعد العمل، أذهب غالبًا للنادي الرياضي.", "B1", 4, "Work"),
    ("Ich bin dafür verantwortlich, das Budget zu verwalten.", "I am responsible for managing the budget.", "أنا مسؤول عن إدارة الميزانية.", "B1", 5, "Work"),
    ("Die Firma bietet flexible Arbeitszeiten an.", "The company offers flexible working hours.", "الشركة تقدم ساعات عمل مرنة.", "B1", 4, "Work"),
    ("Ich habe eine Deadline bis nächsten Freitag.", "I have a deadline until next Friday.", "لدي موعد نهائي حتى الجمعة القادمة.", "B1", 4, "Work"),
    ("Wir müssen die Qualität unserer Produkte verbessern.", "We must improve the quality of our products.", "يجب علينا تحسين جودة منتجاتنا.", "B1", 5, "Work"),
    ("Ich nehme an einer Konferenz über Digitalisierung teil.", "I participate in a conference about digitalization.", "أنا أشارك في مؤتمر حول الرقمنة.", "B1", 5, "Work"),
    ("Das Gehalt wird anhand der Leistung berechnet.", "The salary is calculated based on performance.", "الراتب يُحسب بناءً على الأداء.", "B1", 5, "Work"),
    ("Ich habe einen Termin beim Steuerberater.", "I have an appointment with the tax advisor.", "لدي موعد مع مستشار ضريبي.", "B1", 4, "Work"),
    ("Die Arbeitsbedingungen haben sich verbessert.", "The working conditions have improved.", "ظروف العمل تحسنت.", "B1", 4, "Work"),
    ("Ich bewerbe mich um eine Stelle als Projektmanager.", "I apply for a position as project manager.", "أنا أتقدم لوظيفة كمدير مشاريع.", "B1", 5, "Work"),
    ("Wir feiern das Jubiläum der Firma.", "We celebrate the anniversary of the company.", "نحتفل بالذكرى السنوية للشركة.", "B1", 4, "Work"),
    ("Der Betriebsrat vertritt die Interessen der Mitarbeiter.", "The works council represents the interests of employees.", "مجلس العمل يمثل مصالح الموظفين.", "B1", 5, "Work"),
    ("Ich habe eine Ausbildung als Kaufmann gemacht.", "I completed an apprenticeship as a merchant.", "لقد أكملت تدريبًا مهنيًا كتاجر.", "B1", 5, "Work"),
    ("Die Arbeitslosigkeit ist in dieser Region hoch.", "Unemployment is high in this region.", "البطالة مرتفعة في هذه المنطقة.", "B1", 4, "Work"),
    ("Ich arbeite als freiberuflicher Berater.", "I work as a freelance consultant.", "أنا أعمل كمستشار مستقل.", "B1", 5, "Work"),
    ("Die Firma hat ein neues Bürogebäude eröffnet.", "The company opened a new office building.", "الشركة افتتحت مبنى مكاتب جديد.", "B1", 4, "Work"),
    ("Ich nutze moderne Technologien im Beruf.", "I use modern technologies in my profession.", "أنا أستخدم تقنيات حديثة في مهنتي.", "B1", 5, "Work"),
    ("Die Work-Life-Balance ist mir sehr wichtig.", "Work-life balance is very important to me.", "التوازن بين العمل والحياة مهم جدًا بالنسبة لي.", "B1", 5, "Work"),
    ("Ich habe einen befristeten Arbeitsvertrag.", "I have a temporary employment contract.", "لدي عقد عمل مؤقت.", "B1", 4, "Work"),
    ("Die Gehaltsverhandlung war erfolgreich.", "The salary negotiation was successful.", "مفاوضات الراتب كانت ناجحة.", "B1", 5, "Work"),
    ("Ich arbeite in einem internationalen Team.", "I work in an international team.", "أنا أعمل في فريق دولي.", "B1", 4, "Work"),
    ("Der Chef hat die Prämie für gute Leistung gegeben.", "The boss gave the bonus for good performance.", "المدير أعطى المكافأة للأداء الجيد.", "B1", 5, "Work"),
    ("Ich habe eine Kündigungsfrist von drei Monaten.", "I have a notice period of three months.", "لدي فترة إشعار لمدة ثلاثة أشهر.", "B1", 5, "Work"),
    ("Wir führen ein Mitarbeitergespräch einmal im Monat.", "We conduct an employee meeting once a month.", "نحن نجري اجتماع موظفين مرة في الشهر.", "B1", 5, "Work"),
    ("Ich habe die Zertifizierung in Projektmanagement erhalten.", "I received the certification in project management.", "لقد حصلت على الشهادة في إدارة المشاريع.", "B1", 5, "Work"),
    ("Die Firma bietet Homeoffice an.", "The company offers home office.", "الشركة توفر العمل من المنزل.", "B1", 4, "Work"),
    ("Ich reise geschäftlich oft nach Berlin.", "I travel on business often to Berlin.", "أنا أسافر للعمل غالبًا إلى برلين.", "B1", 5, "Work"),
    ("Die Unternehmenskultur fördert Innovationen.", "The corporate culture promotes innovations.", "ثقافة الشركة تعزز الابتكارات.", "B1", 5, "Work"),
    ("Ich habe einen Mentor, der mich unterstützt.", "I have a mentor who supports me.", "لدي مرشد يدعمني.", "B1", 4, "Work"),
]

# B1 Education (50)
b1_education = [
    ("Ich habe mich entschieden, ein Semester im Ausland zu studieren.", "I decided to study one semester abroad.", "لقد قررت الدراسة لفصل دراسي في الخارج.", "B1", 5, "Education"),
    ("Das Studium erfordert viel Disziplin und Eigeninitiative.", "The studies require a lot of discipline and initiative.", "الدراسة تتطلب الكثير من الانضباط والمبادرة.", "B1", 5, "Education"),
    ("Ich schreibe meine Bachelorarbeit über künstliche Intelligenz.", "I am writing my bachelor thesis about artificial intelligence.", "أنا أكتب أطروحتي الجامعية حول الذكاء الاصطناعي.", "B1", 5, "Education"),
    ("Die Vorlesung findet jeden Dienstag und Donnerstag statt.", "The lecture takes place every Tuesday and Thursday.", "المحاضرة تُعقد كل ثلاثاء وخميس.", "B1", 4, "Education"),
    ("Ich habe mich für drei Kurse eingeschrieben.", "I enrolled in three courses.", "لقد سجلت في ثلاثة مقررات.", "B1", 4, "Education"),
    ("Die Bibliothek ist bis 22 Uhr am Abend geöffnet.", "The library is open until 10 PM in the evening.", "المكتبة مفتوحة حتى الساعة 10 مساءً.", "B1", 4, "Education"),
    ("Ich nehme an einem Erasmus-Programm teil.", "I participate in an Erasmus program.", "أنا أشارك في برنامج إيراسموس.", "B1", 5, "Education"),
    ("Die Prüfungsvorbereitung dauert meistens mehrere Wochen.", "Exam preparation usually takes several weeks.", "التحضير للامتحان يستغرق عادة عدة أسابيع.", "B1", 5, "Education"),
    ("Ich wohne in einem Wohnheim mit anderen Studenten.", "I live in a dormitory with other students.", "أنا أعيش في سكن مع طلاب آخرين.", "B1", 4, "Education"),
    ("Der Professor hat eine interessante Forschungsarbeit veröffentlicht.", "The professor published an interesting research paper.", "الأستاذ نشر ورقة بحثية مثيرة للاهتمام.", "B1", 5, "Education"),
    ("Ich nutze Online-Plattformen für das Selbststudium.", "I use online platforms for self-study.", "أنا أستخدم المنصات الإلكترونية للدراسة الذاتية.", "B1", 5, "Education"),
    ("Die Note im Zeugnis ist sehr wichtig für die Zukunft.", "The grade on the certificate is very important for the future.", "الدرجة في الشهادة مهمة جدًا للمستقبل.", "B1", 5, "Education"),
    ("Ich habe ein Stipendium für hervorragende Leistungen bekommen.", "I received a scholarship for excellent performance.", "حصلت على منحة دراسية للأداء الممتاز.", "B1", 5, "Education"),
    ("Die Gruppenarbeit fördert die sozialen Kompetenzen.", "Group work promotes social skills.", "العمل الجماعي يعزز المهارات الاجتماعية.", "B1", 5, "Education"),
    ("Ich lerne effektiver, wenn ich mir Notizen mache.", "I learn more effectively when I take notes.", "أنا أتعلم بشكل أكثر فعالية عندما آخذ ملاحظات.", "B1", 5, "Education"),
    ("Der Semesterbeginn wird mit einer Party gefeiert.", "The start of the semester is celebrated with a party.", "بداية الفصل الدراسي تحتفل بحفلة.", "B1", 4, "Education"),
    ("Ich habe Prüfungsangst vor der mündlichen Prüfung.", "I have exam anxiety before the oral exam.", "لدي قلق من الامتحان قبل الامتحان الشفوي.", "B1", 4, "Education"),
    ("Die Universität bietet viele Sportkurse an.", "The university offers many sports courses.", "الجامعة تقدم العديد من دورات الرياضة.", "B1", 4, "Education"),
    ("Ich habe mich für ein Praktikum in einem Unternehmen beworben.", "I applied for an internship in a company.", "تقدمت لتدريب داخلي في شركة.", "B1", 5, "Education"),
    ("Das Studium der Medizin dauert mindestens sechs Jahre.", "Studying medicine takes at least six years.", "دراسة الطب تستغرق ست سنوات على الأقل.", "B1", 5, "Education"),
    ("Ich besuche ein Sprachkurs für Fortgeschrittene.", "I attend a language course for advanced learners.", "أنا أحضر دورة لغة للمتعلمين المتقدمين.", "B1", 5, "Education"),
    ("Die Hausarbeit muss eine bestimmte Seitenanzahl haben.", "The term paper must have a certain number of pages.", "الورقة الفصلية يجب أن يكون لها عدد معين من الصفحات.", "B1", 5, "Education"),
    ("Ich nutze die Sprechstunde des Professors.", "I use the professor's office hours.", "أنا أستخدم ساعات مكتب الأستاذ.", "B1", 4, "Education"),
    ("Die Studentenvertretung organisiert viele Events.", "The student council organizes many events.", "مجلس الطلاب ينظم العديد من الفعاليات.", "B1", 5, "Education"),
    ("Ich habe ein Auslandssemester in Spanien geplant.", "I planned a semester abroad in Spain.", "لقد خططت لفصل دراسي في الخارج في إسبانيا.", "B1", 5, "Education"),
    ("Die Lernplattform ist benutzerfreundlich gestaltet.", "The learning platform is designed user-friendly.", "منصة التعلم مصممة بطريقة سهلة الاستخدام.", "B1", 5, "Education"),
    ("Ich muss das Modul bis zum Ende des Semesters abschließen.", "I must complete the module by the end of the semester.", "يجب أن أتم الموديل بحلول نهاية الفصل الدراسي.", "B1", 5, "Education"),
    ("Die Bibliothek bietet auch E-Books zum Ausleihen an.", "The library also offers e-books for borrowing.", "المكتبة تقدم أيضًا كتبًا إلكترونية للإعارة.", "B1", 4, "Education"),
    ("Ich habe ein Forschungsprojekt über Klimawandel gestartet.", "I started a research project about climate change.", "لقد بدأت مشروع بحثي حول تغير المناخ.", "B1", 5, "Education"),
    ("Die Dozentin erklärt die komplexen Themen sehr anschaulich.", "The lecturer explains complex topics very vividly.", "المحاضرة تشرح الموضوعات المعقدة بشكل حيوي جدًا.", "B1", 5, "Education"),
    ("Ich habe die Zulassung für den Masterstudiengang erhalten.", "I received admission for the master's program.", "لقد حصلت على القبول لبرنامج الماجستير.", "B1", 5, "Education"),
    ("Das Studium finanziert sich durch einen Nebenjob.", "The studies are financed through a side job.", "الدراسة تُمول من خلال وظيفة جانبية.", "B1", 5, "Education"),
    ("Ich besuche eine Vorlesung über Wirtschaftspolitik.", "I attend a lecture on economic policy.", "أنا أحضر محاضرة حول السياسة الاقتصادية.", "B1", 5, "Education"),
    ("Die Mensa bietet gesundes Essen zu günstigen Preisen.", "The cafeteria offers healthy food at reasonable prices.", "الكافيتريا تقدم طعامًا صحيًا بأسعار معقولة.", "B1", 4, "Education"),
    ("Ich habe eine Lernpause für eine Woche eingelegt.", "I took a study break for a week.", "لقد أخذت استراحة دراسية لمدة أسبوع.", "B1", 4, "Education"),
    ("Die Abschlussfeier findet in der Aula statt.", "The graduation ceremony takes place in the auditorium.", "حفل التخرج يُعقد في القاعة الكبرى.", "B1", 4, "Education"),
    ("Ich schreibe mir wichtige Informationen in ein Heft.", "I write important information in a notebook.", "أنا أكتب معلومات مهمة في دفتر.", "B1", 4, "Education"),
    ("Die Prüfungsordnung legt die Regeln fest.", "The examination regulations set the rules.", "لوائح الامتحانات تضع القواعد.", "B1", 5, "Education"),
    ("Ich habe einen Tutor, der mir bei Fragen hilft.", "I have a tutor who helps me with questions.", "لدي معلم خصوصي يساعدني في الأسئلة.", "B1", 4, "Education"),
    ("Die Fernuni bietet viele flexible Studiengänge an.", "The distance university offers many flexible study programs.", "الجامعة عن بعد تقدم العديد من برامج الدراسة المرنة.", "B1", 5, "Education"),
    ("Ich habe mich für ein Austauschprogramm beworben.", "I applied for an exchange program.", "تقدمت لبرنامج تبادل.", "B1", 5, "Education"),
    ("Das Studium generale bietet interdisziplinäre Kurse.", "General studies offer interdisciplinary courses.", "الدراسات العامة تقدم مقررات متعددة التخصصات.", "B1", 5, "Education"),
    ("Ich lerne mit Karteikarten Vokabeln.", "I learn vocabulary with flashcards.", "أنا أتعلم المفردات ببطاقات التعلم.", "B1", 4, "Education"),
    ("Die Semesterferien nutze ich für eine Reise.", "I use the semester break for a trip.", "أنا أستخدم عطلة الفصل الدراسي لرحلة.", "B1", 4, "Education"),
    ("Ich habe eine Gruppenarbeit über Geschichte vorbereitet.", "I prepared a group work about history.", "لقد أعددت عملًا جماعيًا حول التاريخ.", "B1", 5, "Education"),
    ("Die Vorlesung wurde aufgrund von Krankheit ausgefallen.", "The lecture was cancelled due to illness.", "المحاضرة أُلغيت بسبب المرض.", "B1", 4, "Education"),
    ("Ich habe ein Zertifikat in Datenanalyse erworben.", "I acquired a certificate in data analysis.", "لقد حصلت على شهادة في تحليل البيانات.", "B1", 5, "Education"),
]

b1_sentences.extend(b1_work)
b1_sentences.extend(b1_education)

print(f"B1 sentences prepared: {len(b1_sentences)}")
print("Add more B1 sentences for other categories...")

# Due to length, we'll write the sentences to a data file
# and then have another script read and generate the final seed file
