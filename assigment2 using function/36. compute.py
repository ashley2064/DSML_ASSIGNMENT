from math import gcd
from functools import reduce

def gcd_of_list(numbers):
    return reduce(gcd, numbers)

nums = [24, 36, 48]
result = gcd_of_list(nums)
print(result)