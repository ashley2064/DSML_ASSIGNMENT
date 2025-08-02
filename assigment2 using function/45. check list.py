def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

numbers = [1, 2, 3, 4]
result = is_sorted(numbers)
print(result) 