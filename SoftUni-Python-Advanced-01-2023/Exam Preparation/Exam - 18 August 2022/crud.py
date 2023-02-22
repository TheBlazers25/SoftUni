def movement(direction_, position_):
    if direction_ == 'left':
        position_[1] -= 1
    elif direction_ == "right":
        position_[1] += 1
    elif direction_ == "up":
        position_[0] -= 1
    elif direction_ == "down":
        position_[0] += 1
    return position_


matrix = []
for _ in range(6):
    matrix.append(input().split())

position = list(map(int, input().strip("(").strip(")").split(", ")))

while True:
    command = input()
    if command == 'Stop':
        break

    current_command = command.split(", ")
    position = movement(current_command[1], position)

    if current_command[0] == 'Create':
        if matrix[position[0]][position[1]] == '.':
            matrix[position[0]][position[1]] = current_command[2]

    if current_command[0] == 'Update':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = current_command[2]

    if current_command[0] == 'Delete':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = '.'

    if current_command[0] == 'Read':
        if matrix[position[0]][position[1]] != '.':
            print(matrix[position[0]][position[1]])

for row in matrix:
    print(" ".join(row))
