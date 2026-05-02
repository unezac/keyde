import json

# Read all sentence data from source files
exec(open('generate_sentences.py', encoding='utf-8').read())
b1_list = b1_sentences

exec(open('generate_b2_sentences.py', encoding='utf-8').read())
b2_list = b2_sentences

exec(open('generate_c1_sentences.py', encoding='utf-8').read())
c1_list = c1_sentences

# Read existing A1+A2 sentences from seed file
with open('seed_all_sentences.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse A1+A2 sentences from the existing file
a1a2_list = []
# Find the sentences list
start = content.find('sentences = [')
end = content.find(']\n\n# Insert in batches')
if end == -1:
    end = content.find(']\n\n# Insert')
list_content = content[start + len('sentences = ['):end].strip()

# Parse each dict manually
import re
dict_pattern = r'\{[^{}]+\}'
for match in re.finditer(dict_pattern, list_content):
    try:
        d = eval(match.group())
        if 'level' in d and d['level'] in ('A1', 'A2'):
            a1a2_list.append(d)
    except:
        pass

print(f"A1+A2: {len(a1a2_list)}")
print(f"B1: {len(b1_list)}")
print(f"B2: {len(b2_list)}")
print(f"C1: {len(c1_list)}")
print(f"Total: {len(a1a2_list) + len(b1_list) + len(b2_list) + len(c1_list)}")

# Write new seed file
all_sentences = a1a2_list + b1_list + b2_list + c1_list

with open('seed_all_sentences.py', 'w', encoding='utf-8') as f:
    f.write('from app.core.database import SessionLocal, engine, Base\n')
    f.write('from app.models import Sentence\n')
    f.write('import random\n\n')
    f.write('Base.metadata.create_all(bind=engine)\n\n')
    f.write('# Check existing sentence count\n')
    f.write('session = SessionLocal()\n')
    f.write('try:\n')
    f.write('    existing_count = session.query(Sentence).count()\n')
    f.write('    if existing_count > 50:\n')
    f.write("        print(f'Database already has {existing_count} sentences (>50), re-seeding anyway.')\n")
    f.write('finally:\n')
    f.write('    session.close()\n\n')
    f.write('# All sentences\n')
    f.write('sentences = [\n')
    
    for s in all_sentences:
        line = f'    {{"german_text": {repr(s["german_text"])}, "english_translation": {repr(s["english_translation"])}, "arabic_translation": {repr(s["arabic_translation"])}, "level": {repr(s["level"])}, "difficulty_score": {s["difficulty_score"]}, "category": {repr(s["category"])}}},\n'
        f.write(line)
    
    f.write(']\n\n')
    
    # Write insert logic
    f.write('# Insert in batches of 100\n')
    f.write('session = SessionLocal()\n')
    f.write('try:\n')
    f.write('    for i in range(0, len(sentences), 100):\n')
    f.write('        batch = sentences[i:i+100]\n')
    f.write('        sentence_objects = [Sentence(**s) for s in batch]\n')
    f.write('        session.bulk_save_objects(sentence_objects)\n')
    f.write('        session.commit()\n')
    f.write("        print(f'Inserted {min(i+100, len(sentences))}/{len(sentences)} sentences...')\n")
    f.write("    print(f'Successfully seeded {len(sentences)} sentences!')\n")
    f.write('except Exception as e:\n')
    f.write('    session.rollback()\n')
    f.write('    print(f"Error: {e}")\n')
    f.write('    raise\n')
    f.write('finally:\n')
    f.write('    session.close()\n')

# Verify syntax
with open('seed_all_sentences.py', 'r', encoding='utf-8') as f:
    new_content = f.read()
compile(new_content, 'seed_all_sentences.py', 'exec')
print('Syntax OK')
