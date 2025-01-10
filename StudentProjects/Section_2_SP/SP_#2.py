with open('snowwhite.txt') as file:
    text = file.read()

sentences = text.split(". ")
corrected_sentences = []

for sentence in sentences:
    sentence = sentence.capitalize()
    corrected_sentences.append(sentence)
    
corrected_text = ". ".join(corrected_sentences)

with open('snowwhite_corrected.txt', 'w') as file:
    file.write(corrected_text)