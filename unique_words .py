sentence = input("input a sentence:")
words = sentence.split()
unique_words = set()
for word in words :
    unique_words.add(word)
for word in unique_words:
    print(word)