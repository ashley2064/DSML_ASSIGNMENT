def merge_dicts(dicts):
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged

dict_list = [{'a': 1}, {'b': 2}, {'a': 3}]
result = merge_dicts(dict_list)
print(result)