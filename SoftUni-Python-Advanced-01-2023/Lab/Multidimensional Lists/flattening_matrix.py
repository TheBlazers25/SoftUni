rows = int(input())
matrix = []

for row in range(rows):
    elements = [int(n) for n in input().split(', ')]
    matrix.append(elements)

    flat_matrix = [num for sublist in matrix for num in sublist]

print(flat_matrix)