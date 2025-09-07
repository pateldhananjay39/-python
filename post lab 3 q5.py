sentence = input("enter a sentence:")
words = sentence.strip().split()
longest_word = max(words, key=len)
if words:
    print("length of last word:", len(words[-1]))
else:
    print("length:", len(longest_word))