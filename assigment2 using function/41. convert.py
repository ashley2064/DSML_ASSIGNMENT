def words_to_ascii(words):
    return [[ord(char) for char in word] for word in words]

words = ["hi"]
result = words_to_ascii(words)
print(result)