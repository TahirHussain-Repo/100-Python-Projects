import os
import re

directory = 'files'

filnames = os.listdir(directory)

all_firsts = []

for filename in filnames:
    filepath = os.path.join(directory, filename)

    with open(filepath, 'r') as file:
        content = file.read()

    pattern = r'[A-za-z0-9,;"\'\s\-()]+[.!?]'
    first_sentences = re.findall(pattern, content)

    if first_sentences:
        all_firsts.append(first_sentences[0])


for sentence in all_firsts:
    print(sentence)

