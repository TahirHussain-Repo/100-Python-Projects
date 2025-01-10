def remove_punctuation(text):
    punctuation = ".,!?:;'\"()[]{}"
    for char in punctuation:
        text = text.replace(char, "")
        return text

text = input("Enter a block of text for analysis: \n")
characters = len(text)
words = len(text.split())
sentences = text.count(".") + text.count("!") + text.count("?")
word_frequency = {} 
word_list = remove_punctuation(text).lower().split()

for word in word_list:
    if not word in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

most_frequent_word = max(word_frequency, key=word_frequency.get)
print(f"\n{word_frequency}")


lengths = [len(word) for word in word_list]
average_word_length = sum(lengths) / len(lengths)
average_sentence_length = words / sentences

print("Text Analysis Results:")
print("-" * 20)
print(f"Total Characters: {characters}")
print(f"Total Words: {words}")
print(f"Total Sentences: {sentences}")
print(f"Most Frequent Word: '{most_frequent_word}' (used {word_frequency[most_frequent_word]} times)")
print(f"Average Word Length: {average_word_length}")
print(f"Average Sentence Length: {average_sentence_length}")
