def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

text = "hello world"
result = count_vowels(text)
print(result)