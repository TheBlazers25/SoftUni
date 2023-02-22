rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
cols = len(matrix[0])

command = input()
while command != 'END':
    command_type, row, col, value = [int(x) if x[-1].isdigit() else x for x in command.split()]

    if 0 <= row < rows and 0 <= col < cols:

        if command_type == 'Add':
            matrix[row][col] += value

        elif command_type == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    command = input()

for row in range(len(matrix)):
    print(" ".join(map(str, matrix[row])))
