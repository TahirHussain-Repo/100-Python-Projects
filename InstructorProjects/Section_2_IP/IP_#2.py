with open('example.txt') as file:
    text = file.read()


words = text.split()
reversed_words = []
for word in words:
    word = word[::-1]
    reversed_words.append(word)

reversed_text = " ".join(reversed_words)
with open('example_reversed.txt', 'w') as file:
    file.write(reversed_text)