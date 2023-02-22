square_matrix_size = int(input())
matrix = []

submarine_health = 3
cruiser_destroyed = 0

for i in range(square_matrix_size):
    row = list(input())
    matrix.append(row)
    if 'S' in row:
        submarine_location = [i, row.index('S')]

while True:
    command = input()
    next_location = []

    if command == 'up':
        next_location = [submarine_location[0] - 1, submarine_location[1]]
    elif command == 'down':
        next_location = [submarine_location[0] + 1, submarine_location[1]]
    elif command == 'left':
        next_location = [submarine_location[0], submarine_location[1] - 1]
    elif command == 'right':
        next_location = [submarine_location[0], submarine_location[1] + 1]

    row, col = next_location[0], next_location[1]
    matrix[submarine_location[0]][submarine_location[1]] = '-'

    if matrix[row][col] == "*":
        matrix[row][col] = "S"
        submarine_health -= 1
        if submarine_health == 0:
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!')
            break

    elif matrix[submarine_location[0]][submarine_location[1]] == "C":
        matrix[row][col] = 'S'
        cruiser_destroyed += 1
        if cruiser_destroyed == 3:
            print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            break

    matrix[row][col] = 'S'
    submarine_location = next_location

for row in matrix:
    print("".join(row))
    