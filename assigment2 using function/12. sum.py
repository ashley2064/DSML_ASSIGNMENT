def sum_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

numbers = [1, 2, 3, 4, 5, 6]
result = sum_even_numbers(numbers)
print(result)