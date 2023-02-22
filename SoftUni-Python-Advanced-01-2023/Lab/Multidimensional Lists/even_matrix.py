rows = int(input())
matrix = []

for row in range(rows):
    elements = [int(n) for n in input().split(', ') if int(n) % 2 == 0]
    matrix.append(elements)

print(matrix)