def char_frequencies(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

text = "banana"
result = char_frequencies(text)
print(result)