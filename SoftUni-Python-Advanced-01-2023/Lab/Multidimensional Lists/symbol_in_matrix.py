rows = int(input())
matrix = []

for row in range(rows):
    elements = list(input())
    matrix.append(elements)

symbol = input()

for i in range(rows):
    if symbol in matrix[i]:
        print(f'({i}, {matrix[i].index(symbol)})')
        break
else:
    print(f'{symbol} does not occur in the matrix')

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         current_element = matrix[i][j]
#         if current_element == symbol:
#             print(f'({i}, {j})')
#             break
# else:
#     print(f'{symbol} does not occur in the matrix')


