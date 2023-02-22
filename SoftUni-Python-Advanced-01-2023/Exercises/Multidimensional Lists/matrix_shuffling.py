rows, columns = [int(n) for n in input().split()]
matrix = []

for row in range(rows):
    elements = input().split()
    matrix.append(elements)

command = input()
while command != 'END':
    command_type, row1, col1, row2, col2 = [int(x) if x.isdigit() else x for x in command.split()]

    if command_type == 'swap':
        if 0 <= row1 < rows and 0 <= col1 < columns and 0 <= row2 < rows and 0 <= col2 < columns:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

            for row in range(len(matrix)):
                print(" ".join(map(str, matrix[row])))

        else:
            print('Invalid input!')
    command = input()
