def filter_by_type(lst, typ):
    return [item for item in lst if isinstance(item, typ)]

items = [1, "a", 2.0, {}, []]
result = filter_by_type(items, str)
print(result)