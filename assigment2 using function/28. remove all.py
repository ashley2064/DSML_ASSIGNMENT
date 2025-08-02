def remove_empty_and_none(lst):
    return [item for item in lst if item != '' and item is not None]

items = [0, 1, "", "hello", None, 5]
result = remove_empty_and_none(items)
print(result)