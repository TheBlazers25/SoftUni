from collections import deque

matrix = []
rover_position = []

water_counter = 0
metal_counter = 0
concrete_counter = 0

for i in range(6):
    row = input().split()
    matrix.append(row)
    if 'E' in row:
        rover_position = [i, row.index('E')]


commands = input().split(', ')

for command in commands:
    if command == 'up':
        if rover_position[0] > 0:
            rover_position[0] -= 1
        else:
            rover_position[0] = 5

    elif command == "down":
        if rover_position[0] < 5:
            rover_position[0] += 1
        else:
            rover_position[0] = 0

    elif command == "left":
        if rover_position[1] > 0:
            rover_position[1] -= 1
        else:
            rover_position[1] = 5

    elif command == "right":
        if rover_position[1] < 5:
            rover_position[1] += 1
        else:
            rover_position[1] = 0

    if matrix[rover_position[0]][rover_position[1]] == 'W':
        print(f'Water deposit found at ({rover_position[0]}, {rover_position[1]})')
        water_counter += 1

    elif matrix[rover_position[0]][rover_position[1]] == 'M':
        print(f'Metal deposit found at ({rover_position[0]}, {rover_position[1]})')
        metal_counter += 1

    elif matrix[rover_position[0]][rover_position[1]] == 'C':
        print(f'Concrete deposit found at ({rover_position[0]}, {rover_position[1]})')
        concrete_counter += 1

    elif matrix[rover_position[0]][rover_position[1]] == 'R':
        print(f'Rover got broken at ({rover_position[0]}, {rover_position[1]})')
        break

if water_counter > 0 and concrete_counter > 0 and metal_counter> 0:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
