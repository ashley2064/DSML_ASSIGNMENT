def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

a = [1, 2, 3]
b = [2, 3, 4]
result = find_common_elements(a, b)
print(result) 