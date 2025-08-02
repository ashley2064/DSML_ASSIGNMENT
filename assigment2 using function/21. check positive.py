def all_positive(lst):
    return all(num > 0 for num in lst)

numbers = [1, 2, 3, -1]
result = all_positive(numbers)
print(result)