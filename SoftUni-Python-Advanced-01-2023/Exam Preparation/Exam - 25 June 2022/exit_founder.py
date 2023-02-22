first_player, second_player = input().split(', ')

matrix = []
for _ in range(6):
    matrix.append(input().split(' '))

first_player_stun = False
second_player_stun = False

while True:
    first_player_coordinates = input()

    if first_player_stun is False:
        row, col = map(int, first_player_coordinates.strip("(").strip(")").split(", "))
        position = matrix[row][col]

        if position == 'E':
            print(f'{first_player} found the Exit and wins the game!')
            break

        if position == 'T':
            print(f'{first_player} is out of the game! The winner is {second_player}.')
            break

        if position == 'W':
            print(f'{first_player} hits a wall and needs to rest.')
            first_player_stun = True
    else:
        first_player_stun = False

    second_player_coordinates = input()
    if second_player_stun is False:
        row, col = map(int, second_player_coordinates.strip("(").strip(")").split(", "))
        position = matrix[row][col]

        if position == 'E':
            print(f'{second_player} found the Exit and wins the game!')
            break

        if position == 'T':
            print(f'{second_player} is out of the game! The winner is {first_player}.')
            break

        if position == 'W':
            print(f'{second_player} hits a wall and needs to rest.')
            second_player_stun = True
    else:
        second_player_stun = False




    # first_player_location = [0, 0]
    # second_player_location = [0, 0]
    #
    # if first_player_move is False and first_player_stun is False:
    #     first_player_location[0], first_player_location[1] = command[0], command[1]
    #     if matrix[first_player_location[0]][first_player_location[1]] == 'E':
    #         print(f'{first_player_location} found the Exit and wins the game!')
    #         break
    #
    #     elif matrix[first_player_location[0]][first_player_location[1]] == '.':
    #         first_player_move = True
    #         continue
    #
    #     elif matrix[first_player_location[0]][first_player_location[1]] == 'W':
    #         print(f'{first_player} hits a wall and needs to rest.')
    #         first_player_move = True
    #         first_player_stun = True
    #
    #     elif matrix[first_player_location[0]][first_player_location[1]] == 'T':
    #         print(f'{first_player} is out of the game! The winner is {second_player}.')
    #
    # elif first_player_move is True:
    #     second_player_location[0], second_player_location[1] = command[0], command[1]
    #     if matrix[second_player_location[0]][second_player_location[1]] == 'E':
    #         print(f'{second_player} found the Exit and wins the game!')
    #         break
    #
    #     elif matrix[second_player_location[0]][second_player_location[1]] == '.':
    #         first_player_move = False
    #         continue
    #
    #     elif matrix[second_player_location[0]][second_player_location[1]] == 'W':
    #         print(f'{second_player} hits a wall and needs to rest.')
    #         first_player_move = False
    #
    #     elif matrix[second_player_location[0]][second_player_location[1]] == 'T':
    #         print(f'{second_player} is out of the game! The winner is {first_player}.')
