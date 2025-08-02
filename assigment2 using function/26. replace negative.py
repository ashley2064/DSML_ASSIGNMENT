def replace_negatives(lst):
    return [num if num >= 0 else 0 for num in lst]

numbers = [-1, 2, -3, 4]
result = replace_negatives(numbers)
print(result)