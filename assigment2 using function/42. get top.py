def top_3_longest(strings):
    return sorted(strings, key=len, reverse=True)[:3]

words = ["a", "abc", "ab", "abcd"]
result = top_3_longest(words)
print(result)