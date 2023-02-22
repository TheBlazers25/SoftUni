rows, columns = [int(n) for n in input().split(', ')]
matrix = []

for row in range(rows):
    elements = [int(n) for n in input().split()]
    matrix.append(elements)

matrix_result = []

for column in range(columns):
    column_sum = 0
    for row_i in range(rows):
        column_sum += matrix[row_i][column]
    matrix_result.append(column_sum)

print(matrix_result)
[print(x) for x in matrix_result]