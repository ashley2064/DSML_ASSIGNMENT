def count_long_words(words):
    return len([word for word in words if len(word) > 5])

words = ["hello", "functional", "map", "filter"]
result = count_long_words(words)
print(result)  