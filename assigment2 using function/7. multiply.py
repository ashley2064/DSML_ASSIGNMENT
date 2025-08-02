from functools import reduce

def multiply_elements(lst):
    return reduce(lambda x, y: x * y, lst)

numbers = [2, 3, 4]
result = multiply_elements(numbers)
print(result)  