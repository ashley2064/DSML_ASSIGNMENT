from functools import reduce


def find_max(lst):
    return reduce(lambda x, y: x if x > y else y, lst)

numbers = [3, 5, 2, 8, 1]
result = find_max(numbers)
print(result) 