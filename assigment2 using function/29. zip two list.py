def zip_lists(list1, list2):
    return list(zip(list1, list2))

a = [1, 2]
b = [3, 4]
result = zip_lists(a, b)
print(result)