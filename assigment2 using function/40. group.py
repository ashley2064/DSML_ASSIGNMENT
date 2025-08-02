def group_by_parity(numbers):
    return {
        "even": [n for n in numbers if n % 2 == 0],
        "odd": [n for n in numbers if n % 2 != 0]
    }

nums = [1, 2, 3, 4, 5]
result = group_by_parity(nums)
print(result)