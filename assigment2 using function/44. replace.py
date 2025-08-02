def replace_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join('*' if char in vowels else char for char in s)

text = "hello"
result = replace_vowels(text)
print(result)