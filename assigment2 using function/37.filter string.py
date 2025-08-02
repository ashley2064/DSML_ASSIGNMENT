def filter_longer_than_avg(strings):
    avg_len = sum(len(s) for s in strings) / len(strings)
    return [s for s in strings if len(s) > avg_len]

words = ["a", "abcd", "abc", "abcdef"]
result = filter_longer_than_avg(words)
print(result)