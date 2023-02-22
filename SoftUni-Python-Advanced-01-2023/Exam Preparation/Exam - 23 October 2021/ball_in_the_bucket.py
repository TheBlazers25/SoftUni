matrix = []

for row in range(6):
    matrix.append(input().split())

points = 0
throw_coordinates = []

for _ in range(3):

    coordinates = list(map(int, input().strip("(").strip(")").split(", ")))
    throw_coordinates = (coordinates[0], coordinates[1])

    if throw_coordinates[0] < 6 and throw_coordinates[1] < 6:
        if matrix[throw_coordinates[0]][throw_coordinates[1]] == 'B':
            matrix[throw_coordinates[0]][throw_coordinates[1]] = 0
            sum_of_points = int(matrix[0][throw_coordinates[1]]) + int(matrix[1][throw_coordinates[1]]) + \
                            int(matrix[2][throw_coordinates[1]]) + int(matrix[3][throw_coordinates[1]]) + \
                            int(matrix[4][throw_coordinates[1]]) + int(matrix[5][throw_coordinates[1]])
            points += sum_of_points
    else:
        continue

if points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")

elif 299 >= points >= 200:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")

elif 199 >= points >= 100:
    print(f"Good job! You scored {points} points, and you've won Football.")

else:
    print(f'Sorry! You need {100 - points} points more to win a prize.')
