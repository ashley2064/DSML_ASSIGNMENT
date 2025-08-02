def combine_lists(lst1, lst2, func):
    return [func(x, y) for x, y in zip(lst1, lst2)]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
f = lambda x, y: x * y

result = combine_lists(list1, list2, f)
print(result)