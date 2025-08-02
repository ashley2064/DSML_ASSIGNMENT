def reverse_strings(words):
    return [word[::-1] for word in words]

words = ["abc", "def"]
result = reverse_strings(words)
print(result)