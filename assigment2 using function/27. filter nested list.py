def filter_sublists_by_sum(nested_list):
    return [sublist for sublist in nested_list if sum(sublist) > 10]

nested = [[1, 2], [5, 6], [10]]
result = filter_sublists_by_sum(nested)
print(result)