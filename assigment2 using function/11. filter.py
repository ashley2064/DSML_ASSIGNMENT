def filter_a_words(words):
    return [word for word in words if word.startswith('a')]

words = ["apple", "banana", "avocado", "cherry"]
result = filter_a_words(words)
print(result)

