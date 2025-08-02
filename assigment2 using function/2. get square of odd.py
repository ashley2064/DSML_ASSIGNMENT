def square_of_odd_numbers(lst):
    return [num**2 for num in lst if num % 2 != 0]

numbers = [1, 2, 3, 4, 5, 6]
result = square_of_odd_numbers(numbers)
print(result)

