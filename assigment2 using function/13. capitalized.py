def capitalize_words(words):
    return [word.capitalize() for word in words]

words = ["hello", "world"]
result = capitalize_words(words)
print(result)