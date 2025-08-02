from functools import reduce

def sum_elements(lst):
    return reduce(lambda x, y: x + y, lst)

numbers = [1, 2, 3, 4]
result = sum_elements(numbers)
print(result)  # Output: 1