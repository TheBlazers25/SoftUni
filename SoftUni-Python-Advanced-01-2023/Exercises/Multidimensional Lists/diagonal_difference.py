rows = int(input())
matrix = []

for row in range(rows):
    elements = [int(n) for n in input().split()]
    matrix.append(elements)

primary_diagonal_sum = 0
primary_diagonal = []

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            primary_diagonal.append(matrix[i][j])
            primary_diagonal_sum += matrix[i][j]

secondary_diagonal_sum = 0
secondary_diagonal = []

for i in range(len(matrix) - 1, -1, -1):
    secondary_diagonal.append(matrix[i][(len(matrix) - 1) - i])
    secondary_diagonal_sum += matrix[i][(len(matrix) - 1) - i]

secondary_diagonal.reverse()
print(abs(primary_diagonal_sum - secondary_diagonal_sum))
