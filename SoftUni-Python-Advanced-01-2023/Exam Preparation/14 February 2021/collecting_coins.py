import math

field_size = int(input())

matrix = []
for _ in range(field_size):
    matrix.append(input().split())

player_position = []
for row in range(field_size):
    for col in range(field_size):
        if matrix[row][col] == "P":
            player_position = [row, col]
            first_position = [row, col]

path = [first_position]
coins = 0
game_won = False

while True:

    if coins >= 100:
        game_won = True
        break

    direction = input()

    if direction == "up":
        if player_position[0] > 0:
            player_position[0] -= 1
        else:
            player_position[0] = field_size - 1

    elif direction == "down":
        if player_position[0] < field_size - 1:
            player_position[0] += 1
        else:
            player_position[0] = 0

    elif direction == "left":
        if player_position[1] > 0:
            player_position[1] -= 1
        else:
            player_position[1] = field_size - 1

    elif direction == "right":
        if player_position[1] < field_size - 1:
            player_position[1] += 1
        else:
            player_position[1] = 0

    current_position = matrix[player_position[0]][player_position[1]]
    path.append([player_position[0], player_position[1]])

    if current_position.isnumeric():
        coins += int(current_position)
        matrix[player_position[0]][player_position[1]] = '0'

    elif matrix[player_position[0]][player_position[1]] == 'X':
        coins /= 2
        break

if game_won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {math.floor(coins)} coins.")

print('Your path:')
print(*path, sep='\n')

