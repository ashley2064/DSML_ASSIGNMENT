def first_letters(words):
    return [word[0] for word in words if word]

words = ["cat", "dog", "elephant"]
result = first_letters(words)
print(result)