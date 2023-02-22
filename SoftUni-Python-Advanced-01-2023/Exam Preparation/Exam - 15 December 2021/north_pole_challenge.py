rows, columns = [int(n) for n in input().split(', ')]

matrix = []
for row in range(rows):
    matrix.append(input().split())

all_items = {'christmas_decorations': 0, 'gifts': 0, 'cookies': 0}

current_position = []
for row in range(rows):
    for col in range(columns):
        if matrix[row][col] == "Y":
            current_position = [row, col]
            matrix[row][col] = 'x'

        if matrix[row][col] == "G":
            all_items['gifts'] += 1

        if matrix[row][col] == "C":
            all_items['cookies'] += 1

        if matrix[row][col] == "D":
            all_items['christmas_decorations'] += 1

all_items_sum = sum(all_items.values())

christmas_decorations = 0
cookies = 0
gifts = 0

collected_all = False

while True:

    if all_items_sum == 0:
        collected_all = True
        break

    command = input()

    if command == 'End':
        break

    direction, steps = command.split('-')
    steps = int(steps)

    for step in range(steps):

        if all_items_sum == 0:
            collected_all = True
            break

        if direction == "up":
            if current_position[0] > 0:
                current_position[0] -= 1
            else:
                current_position[0] = rows - 1

        elif direction == "down":
            if current_position[0] < rows - 1:
                current_position[0] += 1
            else:
                current_position[0] = 0

        elif direction == "left":
            if current_position[1] > 0:
                current_position[1] -= 1
            else:
                current_position[1] = columns - 1

        elif direction == "right":
            if current_position[1] < columns - 1:
                current_position[1] += 1
            else:
                current_position[1] = 0

        if matrix[current_position[0]][current_position[1]] == 'D':
            matrix[current_position[0]][current_position[1]] = 'x'
            christmas_decorations += 1
            all_items_sum -= 1

        elif matrix[current_position[0]][current_position[1]] == 'G':
            matrix[current_position[0]][current_position[1]] = 'x'
            gifts += 1
            all_items_sum -= 1

        elif matrix[current_position[0]][current_position[1]] == 'C':
            matrix[current_position[0]][current_position[1]] = 'x'
            cookies += 1
            all_items_sum -= 1

        matrix[current_position[0]][current_position[1]] = 'x'

matrix[current_position[0]][current_position[1]] = 'Y'

if collected_all is True:
    print('Merry Christmas!')

print(f"You've collected:\n- {christmas_decorations} Christmas decorations"
      f"\n- {gifts} Gifts"
      f"\n- {cookies} Cookies")

for row in range(len(matrix)):
    print(" ".join(matrix[row]))
