def running_total(lst):
    totals = []
    current_sum = 0
    for num in lst:
        current_sum += num
        totals.append(current_sum)
    return totals

numbers = [1, 2, 3, 4]
result = running_total(numbers)
print(result)