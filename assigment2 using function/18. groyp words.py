def group_by_length(words):
    grouped = {}
    for word in words:
        length = len(word)
        grouped.setdefault(length, []).append(word)
    return grouped

words = ["hi", "hello", "yes", "no", "code"]
result = group_by_length(words)
print(result)
