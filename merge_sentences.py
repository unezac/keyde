# Read existing seed file
with open('seed_all_sentences.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the closing bracket of sentences list
closing_line = None
for i, line in enumerate(lines):
    if line.strip() == ']' and i < 722:  # Before the insert section
        closing_line = i
        break

# Find where B1 section starts in the file (after A2)
# We know A1+A2 end at line 709 (line 721 in 1-indexed = ])
# So we need to insert before the closing bracket

# Read B1 sentences
with open('generate_sentences.py', 'r', encoding='utf-8') as f:
    b1_content = f.read()
b1_start = b1_content.find('b1_sentences = [')
b1_end = b1_content.find(']', b1_start) + 1
b1_data = b1_content[b1_start:b1_end]

# Read B2 sentences
with open('generate_b2_sentences.py', 'r', encoding='utf-8') as f:
    b2_content = f.read()
b2_start = b2_content.find('b2_sentences = [')
b2_end = b2_content.find(']', b2_start) + 1
b2_data = b2_content[b2_start:b2_end]

# Read C1 sentences
with open('generate_c1_sentences.py', 'r', encoding='utf-8') as f:
    c1_content = f.read()
c1_start = c1_content.find('c1_sentences = [')
c1_end = c1_content.find(']', c1_start) + 1
c1_data = c1_content[c1_start:c1_end]

# Replace variable names
b1_data = b1_data.replace('b1_sentences', 'temp_list1')
b2_data = b2_data.replace('b2_sentences', 'temp_list2')
c1_data = c1_data.replace('c1_sentences', 'temp_list3')

# Execute to get the lists
exec(b1_data)
exec(b2_data)
exec(c1_data)

# Count sentences
print(f"A1+A2: {len(lines)} lines")
print(f"B1: {len(temp_list1)}")
print(f"B2: {len(temp_list2)}")
print(f"C1: {len(temp_list3)}")
print(f"Total expected: {702 + len(temp_list1) + len(temp_list2) + len(temp_list3)}")

# Now let's just append to the existing list
# Find the position of the last ] before the insert section
insert_pos = None
for i in range(len(lines) - 1, -1, -1):
    if '# Insert in batches' in lines[i]:
        for j in range(i, -1, -1):
            if lines[j].strip() == ']':
                insert_pos = j
                break
        break

print(f"Insert position: line {insert_pos + 1}")

# Build new content
new_lines = []
new_lines.extend(lines[:insert_pos])

# Add B1 sentences
for s in temp_list1:
    line = f'    {{"german_text": {repr(s["german_text"])}, "english_translation": {repr(s["english_translation"])}, "arabic_translation": {repr(s["arabic_translation"])}, "level": {repr(s["level"])}, "difficulty_score": {s["difficulty_score"]}, "category": {repr(s["category"])}}},\n'
    new_lines.append(line)

# Add B2 sentences
for s in temp_list2:
    line = f'    {{"german_text": {repr(s["german_text"])}, "english_translation": {repr(s["english_translation"])}, "arabic_translation": {repr(s["arabic_translation"])}, "level": {repr(s["level"])}, "difficulty_score": {s["difficulty_score"]}, "category": {repr(s["category"])}}},\n'
    new_lines.append(line)

# Add C1 sentences
for s in temp_list3:
    line = f'    {{"german_text": {repr(s["german_text"])}, "english_translation": {repr(s["english_translation"])}, "arabic_translation": {repr(s["arabic_translation"])}, "level": {repr(s["level"])}, "difficulty_score": {s["difficulty_score"]}, "category": {repr(s["category"])}}},\n'
    new_lines.append(line)

# Add closing bracket and rest of file
new_lines.append(']\n')
new_lines.extend(lines[insert_pos + 1:])

# Write
with open('seed_all_sentences.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Total lines written: {len(new_lines)}")
