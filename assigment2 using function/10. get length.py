def word_lengths(words):
    return list(map(len, words))

words = ["hi", "there", "world"]
lengths = word_lengths(words)
print(lengths)