first_player, second_player = input().split(', ')

matrix = []
for _ in range(7):
    matrix.append(input().split())

first_player_score = 501
second_player_score = 501

first_player_throws = 0
second_player_throws = 0

while True:

    row, col = [int(x) for x in input()[1:-1].split(", ")]
    if 0 <= row <= 7 and 0 <= col < 7:
        dart_position = matrix[row][col]
        first_player_throws += 1

        if dart_position.isnumeric():
            first_player_score -= int(dart_position)

        elif dart_position == 'B':
            print(f'{first_player} won the game with {first_player_throws} throws!')
            break

        elif dart_position == 'D':
            points_to_deduct = (int(matrix[0][col]) + int(matrix[-1][col]) + int(matrix[row][0]) + int(matrix[row][-1])) * 2
            first_player_score -= points_to_deduct

        elif dart_position == 'T':
            points_to_deduct = (int(matrix[0][col]) + int(matrix[-1][col]) + int(matrix[row][0]) + int(matrix[row][-1])) * 3
            first_player_score -= points_to_deduct

        if first_player_score <= 0:
            print(f'{first_player} won the game with {first_player_throws} throws!')
            break

    row, col = [int(x) for x in input()[1:-1].split(", ")]
    if 0 <= row <= 7 and 0 <= col < 7:
        dart_position = matrix[row][col]
        second_player_throws += 1

        if dart_position.isnumeric():
            second_player_score -= int(dart_position)

        elif dart_position == 'B':
            print(f'{second_player} won the game with {second_player_throws} throws!')
            break

        elif dart_position == 'D':
            points_to_deduct = (int(matrix[0][col]) + int(matrix[-1][col]) + int(matrix[row][0]) + int(matrix[row][-1])) * 2
            second_player_score -= points_to_deduct

        elif dart_position == 'T':
            points_to_deduct = (int(matrix[0][col]) + int(matrix[-1][col]) + int(matrix[row][0]) + int(matrix[row][-1])) * 3
            second_player_score -= points_to_deduct

        if second_player_score <= 0:
            print(f'{second_player} won the game with {second_player_throws} throws!')
            break
