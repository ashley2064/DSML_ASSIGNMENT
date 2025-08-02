def filter_integers(lst):
    return [x for x in lst if isinstance(x, int)]

items = [1, "a", 2.5, 3, "b"]
result = filter_integers(items)
print(result)