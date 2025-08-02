def remove_digits(s):
    return ''.join(char for char in s if not char.isdigit())

text = "a1b2c3"
result = remove_digits(text)
print(result)