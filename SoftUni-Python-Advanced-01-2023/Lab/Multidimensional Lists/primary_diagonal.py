rows = int(input())
matrix = []

for row in range(rows):
    elements = [int(n) for n in input().split()]
    matrix.append(elements)

diagonal_sum = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            diagonal_sum += matrix[i][j]

print(diagonal_sum)