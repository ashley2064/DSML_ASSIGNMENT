def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [[1, 2], [3, 4]]
result = transpose(matrix)
print(result)
