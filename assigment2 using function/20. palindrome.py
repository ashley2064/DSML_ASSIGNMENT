def find_palindromes(words):
    return [word for word in words if word == word[::-1]]

words = ["madam", "hello", "noon"]
result = find_palindromes(words)
print(result)