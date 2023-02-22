rows, columns = [int(n) for n in input().split(', ')]
matrix = []

for row in range(rows):
    elements = [int(n) for n in input().split(', ')]
    matrix.append([])

    for column in range(columns):
        matrix[row].append(elements[column])

print(sum([sum(i) for i in zip(*matrix)]))
print(matrix)