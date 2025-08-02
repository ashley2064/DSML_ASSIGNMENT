from collections import Counter

def most_frequent_word(words):
    count = Counter(words)
    return count.most_common(1)[0][0]

words = ["a", "b", "a", "c", "a"]
result = most_frequent_word(words)
print(result)