-- KeyGermany Database Schema

CREATE TABLE IF NOT EXISTS sentences (
    id SERIAL PRIMARY KEY,
    german_text TEXT NOT NULL,
    english_translation TEXT NOT NULL,
    arabic_translation TEXT NOT NULL,
    level VARCHAR(5) DEFAULT 'B2',
    difficulty_score INTEGER CHECK (difficulty_score >= 1 AND difficulty_score <= 10),
    category VARCHAR(50) DEFAULT 'Daily Life',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_sentences_level ON sentences(level);
CREATE INDEX IF NOT EXISTS idx_sentences_category ON sentences(category);

CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_sentences_updated_at ON sentences;
CREATE TRIGGER trg_sentences_updated_at
BEFORE UPDATE ON sentences
FOR EACH ROW
EXECUTE FUNCTION set_updated_at();

-- B2 German practice sentences for typing, listening, and translation.
INSERT INTO sentences (german_text, english_translation, arabic_translation, level, difficulty_score) VALUES
('Obwohl das Wetter schlecht war, haben wir einen langen Spaziergang im Wald gemacht.', 'Although the weather was bad, we took a long walk in the forest.', 'على الرغم من أن الطقس كان سيئاً، قمنا بنزهة طويلة في الغابة.', 'B2', 6),
('Es ist wichtig, dass wir uns regelmäßig über die neuesten Entwicklungen in der Technologie informieren.', 'It is important that we regularly inform ourselves about the latest developments in technology.', 'من المهم أن نطلع بانتظام على أحدث التطورات في التكنولوجيا.', 'B2', 7),
('Je mehr man übt, desto besser wird man beim Erlernen einer neuen Sprache.', 'The more you practice, the better you become at learning a new language.', 'كلما تدرب المرء أكثر، أصبح أفضل في تعلم لغة جديدة.', 'B2', 5),
('Trotz der Schwierigkeiten hat er es geschafft, seine Ziele rechtzeitig zu erreichen.', 'Despite the difficulties, he managed to achieve his goals on time.', 'على الرغم من الصعوبات، تمكن من تحقيق أهدافه في الوقت المحدد.', 'B2', 6),
('Ich hätte mich gefreut, wenn du mich früher über deine Entscheidung informiert hättest.', 'I would have been happy if you had informed me earlier about your decision.', 'كنت سأكون سعيداً لو أخبرتني بقرارك في وقت سابق.', 'B2', 8),
('Die meisten Menschen unterschätzen, wie viel Zeit man für die Vorbereitung einer Präsentation benötigt.', 'Most people underestimate how much time is needed to prepare a presentation.', 'يقلل معظم الناس من تقدير الوقت اللازم لإعداد عرض تقديمي.', 'B2', 7),
('Wenn ich mehr Zeit hätte, würde ich mich intensiver mit der deutschen Geschichte beschäftigen.', 'If I had more time, I would study German history more intensively.', 'لو كان لدي وقت أكثر، لاهتممت بالتاريخ الألماني بشكل أعمق.', 'B2', 7),
('Es wird empfohlen, täglich mindestens zwei Liter Wasser zu trinken, um gesund zu bleiben.', 'It is recommended to drink at least two liters of water daily to stay healthy.', 'يوصى بشرب لترين من الماء على الأقل يومياً للحفاظ على الصحة.', 'B2', 5),
('Anstatt fernzusehen, sollten wir öfter ein Buch lesen oder nach draußen gehen.', 'Instead of watching television, we should read a book or go outside more often.', 'بدلاً من مشاهدة التلفاز، ينبغي أن نقرأ كتاباً أو نخرج أكثر.', 'B2', 5),
('Wir müssen sicherstellen, dass alle Teilnehmer die Regeln des Wettbewerbs verstanden haben.', 'We must ensure that all participants have understood the rules of the competition.', 'يجب أن نتأكد من أن جميع المشاركين فهموا قواعد المسابقة.', 'B2', 6),
('Nachdem sie die Prüfung bestanden hatte, bewarb sie sich sofort um ein Praktikum in Berlin.', 'After she had passed the exam, she immediately applied for an internship in Berlin.', 'بعد أن نجحت في الامتحان، تقدمت فوراً للحصول على تدريب في برلين.', 'B2', 6),
('Der Zug hatte Verspätung, weshalb viele Reisende ihre Anschlussverbindungen verpasst haben.', 'The train was delayed, which is why many travelers missed their connecting trains.', 'تأخر القطار، ولذلك فاتت الكثير من المسافرين رحلاتهم التالية.', 'B2', 7),
('Man sollte soziale Medien bewusst nutzen, damit sie nicht zu viel Aufmerksamkeit beanspruchen.', 'One should use social media consciously so that it does not demand too much attention.', 'ينبغي استخدام وسائل التواصل الاجتماعي بوعي حتى لا تستحوذ على الكثير من الانتباه.', 'B2', 7),
('Die Firma sucht Mitarbeiter, die sowohl zuverlässig als auch kreativ arbeiten können.', 'The company is looking for employees who can work both reliably and creatively.', 'تبحث الشركة عن موظفين يستطيعون العمل بموثوقية وإبداع في الوقت نفسه.', 'B2', 5),
('Falls du Fragen hast, kannst du dich jederzeit an die zuständige Abteilung wenden.', 'If you have questions, you can contact the responsible department at any time.', 'إذا كانت لديك أسئلة، يمكنك التواصل مع القسم المسؤول في أي وقت.', 'B2', 5),
('Seitdem ich regelmäßig Nachrichten höre, verstehe ich gesprochene deutsche Texte deutlich besser.', 'Since I started listening to the news regularly, I understand spoken German texts much better.', 'منذ أن بدأت أستمع إلى الأخبار بانتظام، صرت أفهم النصوص الألمانية المنطوقة بشكل أفضل.', 'B2', 6),
('Die Wohnung ist zwar klein, aber sie liegt zentral und ist gut an den Verkehr angebunden.', 'The apartment is small, but it is centrally located and well connected to transport.', 'الشقة صغيرة، لكنها تقع في موقع مركزي ومتصلة جيداً بوسائل النقل.', 'B2', 5),
('Viele Städte investieren in Fahrradwege, um den Verkehr umweltfreundlicher zu gestalten.', 'Many cities invest in bike lanes to make traffic more environmentally friendly.', 'تستثمر مدن كثيرة في مسارات الدراجات لجعل حركة المرور أكثر صداقة للبيئة.', 'B2', 6),
('Bevor man einen Vertrag unterschreibt, sollte man alle Bedingungen sorgfältig lesen.', 'Before signing a contract, one should read all conditions carefully.', 'قبل توقيع عقد، ينبغي قراءة جميع الشروط بعناية.', 'B2', 5),
('Die Lehrerin erklärte den Unterschied noch einmal, damit niemand verwirrt blieb.', 'The teacher explained the difference once more so that no one remained confused.', 'شرحت المعلمة الفرق مرة أخرى حتى لا يبقى أحد مرتبكاً.', 'B2', 5),
('Obwohl er wenig geschlafen hatte, hielt er eine überzeugende Rede vor dem Publikum.', 'Although he had slept little, he gave a convincing speech in front of the audience.', 'رغم أنه نام قليلاً، ألقى خطاباً مقنعاً أمام الجمهور.', 'B2', 7),
('Die Entscheidung wurde verschoben, weil noch wichtige Informationen fehlten.', 'The decision was postponed because important information was still missing.', 'تم تأجيل القرار لأن معلومات مهمة كانت لا تزال ناقصة.', 'B2', 5),
('Wer regelmäßig Sport treibt, kann Stress abbauen und seine Konzentration verbessern.', 'Those who exercise regularly can reduce stress and improve their concentration.', 'من يمارس الرياضة بانتظام يستطيع تقليل التوتر وتحسين التركيز.', 'B2', 5),
('Die Kundin beschwerte sich, nachdem das bestellte Paket beschädigt angekommen war.', 'The customer complained after the ordered package arrived damaged.', 'اشتكت الزبونة بعد أن وصلت الحزمة المطلوبة تالفة.', 'B2', 6),
('Damit das Projekt erfolgreich wird, müssen alle Teammitglieder offen miteinander kommunizieren.', 'For the project to succeed, all team members must communicate openly with each other.', 'لكي ينجح المشروع، يجب أن يتواصل جميع أعضاء الفريق بصراحة مع بعضهم.', 'B2', 7),
('Die Regierung plant neue Maßnahmen, um bezahlbaren Wohnraum in Großstädten zu schaffen.', 'The government is planning new measures to create affordable housing in big cities.', 'تخطط الحكومة لإجراءات جديدة لتوفير سكن بأسعار معقولة في المدن الكبرى.', 'B2', 8),
('Während des Gesprächs stellte sich heraus, dass beide Seiten ähnliche Interessen hatten.', 'During the conversation, it turned out that both sides had similar interests.', 'أثناء الحديث، تبين أن الطرفين لديهما مصالح متشابهة.', 'B2', 6),
('Ich finde es beeindruckend, wie schnell Kinder neue Wörter in einer Fremdsprache aufnehmen.', 'I find it impressive how quickly children absorb new words in a foreign language.', 'أجد من المثير للإعجاب مدى سرعة اكتساب الأطفال لكلمات جديدة بلغة أجنبية.', 'B2', 6),
('Der Artikel beschreibt, welche Auswirkungen künstliche Intelligenz auf den Arbeitsmarkt haben könnte.', 'The article describes what effects artificial intelligence could have on the labor market.', 'يصف المقال الآثار التي قد يحدثها الذكاء الاصطناعي في سوق العمل.', 'B2', 8),
('Nachdem der Computer neu gestartet wurde, funktionierte das Programm wieder ohne Probleme.', 'After the computer was restarted, the program worked again without problems.', 'بعد إعادة تشغيل الحاسوب، عمل البرنامج مرة أخرى دون مشاكل.', 'B2', 5),
('Es lohnt sich, frühzeitig mit dem Lernen zu beginnen, statt alles bis zuletzt aufzuschieben.', 'It is worth starting to study early instead of postponing everything until the end.', 'من المفيد البدء في التعلم مبكراً بدلاً من تأجيل كل شيء إلى النهاية.', 'B2', 6),
('Die Ärztin riet ihm, sich mehr zu bewegen und seine Ernährung langsam umzustellen.', 'The doctor advised him to move more and gradually change his diet.', 'نصحته الطبيبة بأن يتحرك أكثر وأن يغير نظامه الغذائي تدريجياً.', 'B2', 6),
('Viele Menschen wünschen sich flexible Arbeitszeiten, damit sie Beruf und Familie besser verbinden können.', 'Many people want flexible working hours so they can better combine work and family.', 'يرغب كثير من الناس في ساعات عمل مرنة حتى يوفقوا بين العمل والأسرة بشكل أفضل.', 'B2', 7),
('Der Film war spannend, obwohl einige Szenen vorhersehbar und etwas zu lang waren.', 'The film was exciting, although some scenes were predictable and a bit too long.', 'كان الفيلم مشوقاً، رغم أن بعض المشاهد كانت متوقعة وطويلة قليلاً.', 'B2', 5),
('Um Missverständnisse zu vermeiden, sollten wichtige Absprachen schriftlich festgehalten werden.', 'To avoid misunderstandings, important agreements should be recorded in writing.', 'لتجنب سوء الفهم، ينبغي توثيق الاتفاقات المهمة كتابياً.', 'B2', 7),
('Die Stadtbibliothek bietet kostenlose Kurse an, in denen Erwachsene digitale Kompetenzen erwerben können.', 'The city library offers free courses where adults can acquire digital skills.', 'تقدم مكتبة المدينة دورات مجانية يستطيع فيها البالغون اكتساب مهارات رقمية.', 'B2', 8),
('Sobald die Ergebnisse veröffentlicht werden, erhalten alle Bewerber eine Nachricht per E-Mail.', 'As soon as the results are published, all applicants receive a message by email.', 'بمجرد نشر النتائج، يتلقى جميع المتقدمين رسالة عبر البريد الإلكتروني.', 'B2', 6),
('Die Nachbarn halfen einander, als nach dem Sturm mehrere Keller unter Wasser standen.', 'The neighbors helped one another when several basements were flooded after the storm.', 'ساعد الجيران بعضهم بعضاً عندما غمرت المياه عدة أقبية بعد العاصفة.', 'B2', 7),
('Es fällt mir leichter, neue Grammatik zu verstehen, wenn ich viele Beispiele sehe.', 'It is easier for me to understand new grammar when I see many examples.', 'يسهل علي فهم القواعد الجديدة عندما أرى أمثلة كثيرة.', 'B2', 5),
('Die Diskussion zeigte, dass nachhaltige Lösungen oft Geduld und Kompromissbereitschaft erfordern.', 'The discussion showed that sustainable solutions often require patience and willingness to compromise.', 'أظهرت المناقشة أن الحلول المستدامة تتطلب غالباً الصبر والاستعداد للتنازل.', 'B2', 8),
('Obwohl die Aufgabe kompliziert aussah, konnte sie mit einer klaren Strategie gelöst werden.', 'Although the task looked complicated, it could be solved with a clear strategy.', 'رغم أن المهمة بدت معقدة، أمكن حلها باستراتيجية واضحة.', 'B2', 6),
('Der Verkäufer versprach, das defekte Gerät innerhalb einer Woche zu reparieren.', 'The seller promised to repair the defective device within one week.', 'وعد البائع بإصلاح الجهاز المعطل خلال أسبوع واحد.', 'B2', 5),
('Wer im Ausland studieren möchte, sollte sich rechtzeitig über Visa und Versicherungen informieren.', 'Anyone who wants to study abroad should inform themselves about visas and insurance in good time.', 'من يريد الدراسة في الخارج ينبغي أن يستعلم مبكراً عن التأشيرات والتأمينات.', 'B2', 7),
('Die Konferenz wurde online übertragen, damit auch internationale Gäste teilnehmen konnten.', 'The conference was streamed online so that international guests could also participate.', 'تم بث المؤتمر عبر الإنترنت حتى يتمكن الضيوف الدوليون أيضاً من المشاركة.', 'B2', 6),
('Manchmal erkennt man erst später, welche Erfahrungen wirklich wichtig gewesen sind.', 'Sometimes one only recognizes later which experiences were truly important.', 'أحياناً لا يدرك المرء إلا لاحقاً أي التجارب كانت مهمة حقاً.', 'B2', 6),
('Die Eltern unterstützten ihre Tochter, obwohl sie ihre Entscheidung zunächst nicht verstanden.', 'The parents supported their daughter although they did not understand her decision at first.', 'دعم الوالدان ابنتهما رغم أنهما لم يفهما قرارها في البداية.', 'B2', 6),
('Der Bericht fasst zusammen, warum erneuerbare Energien langfristig immer wichtiger werden.', 'The report summarizes why renewable energies are becoming increasingly important in the long term.', 'يلخص التقرير لماذا تصبح الطاقات المتجددة أكثر أهمية على المدى الطويل.', 'B2', 7),
('Wenn alle pünktlich erscheinen, können wir die Besprechung ohne Verzögerung beginnen.', 'If everyone arrives on time, we can begin the meeting without delay.', 'إذا حضر الجميع في الوقت المحدد، يمكننا بدء الاجتماع دون تأخير.', 'B2', 5),
('Die Sprachschule empfiehlt, jeden Tag kurze Texte zu schreiben und laut vorzulesen.', 'The language school recommends writing short texts every day and reading them aloud.', 'توصي مدرسة اللغة بكتابة نصوص قصيرة كل يوم وقراءتها بصوت عال.', 'B2', 5),
('Nachdem die Software aktualisiert worden war, standen mehrere nützliche Funktionen zur Verfügung.', 'After the software had been updated, several useful features were available.', 'بعد تحديث البرنامج، أصبحت عدة وظائف مفيدة متاحة.', 'B2', 6),
('Die Mitarbeiterin bat um Rückmeldung, bevor sie den endgültigen Bericht abschickte.', 'The employee asked for feedback before sending the final report.', 'طلبت الموظفة ملاحظات قبل أن ترسل التقرير النهائي.', 'B2', 5),
('Ob man erfolgreich lernt, hängt nicht nur vom Talent, sondern auch von Gewohnheiten ab.', 'Whether one learns successfully depends not only on talent, but also on habits.', 'لا يعتمد التعلم الناجح على الموهبة فقط، بل يعتمد أيضاً على العادات.', 'B2', 7),
('Der Kurs richtet sich an Lernende, die ihre Aussprache und ihre Schreibsicherheit verbessern möchten.', 'The course is aimed at learners who want to improve their pronunciation and writing confidence.', 'تستهدف الدورة المتعلمين الذين يريدون تحسين نطقهم وثقتهم في الكتابة.', 'B2', 6),
('In vielen Berufen ist es notwendig, komplexe Informationen verständlich zusammenzufassen.', 'In many professions it is necessary to summarize complex information clearly.', 'في كثير من المهن، من الضروري تلخيص المعلومات المعقدة بوضوح.', 'B2', 7),
('Die Erfahrung hat gezeigt, dass kleine tägliche Fortschritte langfristig große Wirkung haben.', 'Experience has shown that small daily improvements have a big long-term effect.', 'أظهرت التجربة أن التقدم اليومي الصغير يترك أثراً كبيراً على المدى الطويل.', 'B2', 6);
