def strings_with_numbers(lst):
    return [s for s in lst if any(char.isdigit() for char in s)]

strings = ["abc", "123", "a1b2", "xyz"]
result = strings_with_numbers(strings)
print(result)