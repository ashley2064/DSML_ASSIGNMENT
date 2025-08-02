def count_frequencies(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    return freq

numbers = [1, 2, 2, 3, 1, 1]
result = count_frequencies(numbers)
print(result)