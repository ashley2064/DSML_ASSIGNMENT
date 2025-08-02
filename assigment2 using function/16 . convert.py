def celsius_to_fahrenheit(celsius_list):
    return [round(c * 9/5 + 32, 1) for c in celsius_list]

temps = [0, 100, 37]
result = celsius_to_fahrenheit(temps)
print(result)