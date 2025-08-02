def convert_nested_to_int(nested_list):
    return [[int(item) for item in sublist] for sublist in nested_list]

nested_strings = [["1", "2"], ["3", "4"]]
result = convert_nested_to_int(nested_strings)
print(result)