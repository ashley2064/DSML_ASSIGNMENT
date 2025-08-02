from itertools import permutations

def get_permutations(lst):
    return [list(p) for p in permutations(lst)]

numbers = [1, 2, 3]
result = get_permutations(numbers)
print(result)
