from functools import reduce

def remove_duplicates(lst):
    return reduce(lambda acc, x: acc + [x] if x not in acc else acc, lst, [])

numbers = [1, 2, 2, 3, 1]
result = remove_duplicates(numbers)
print(result)  