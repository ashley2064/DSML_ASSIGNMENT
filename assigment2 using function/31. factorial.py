from functools import reduce

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

result = factorial(5)
print(result)