def store_pieces(number):
    data = {}
    for _ in range(number):
        piece_data = input().split('|')
        piece = piece_data[0]
        composer = piece_data[1]
        key = piece_data[2]

        data[piece] = [composer, key]

    return data


def add_pieces(piece, composer, key, data):
    if piece not in data:
        data[piece] = [composer, key]
        print(f'{piece} by {composer} in {key} added to the collection!')
    else:
        print(f'{piece} is already in the collection!')


def remove_pieces(piece, data):
    if piece in data:
        del data[piece]
        print(f'Successfully removed {piece}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')


def changekey(piece, new_key, data):
    if piece in data:
        data[piece][1] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')


def print_pieces(data):
    result = ''
    for piece in data:
        composer = data[piece][0]
        key = data[piece][1]
        result += f'{piece} -> Composer: {composer}, Key: {key}\n'

    return result


def pianist_func(number):

    data = store_pieces(number)

    while True:
        command = input().split('|')
        main_command = command[0]

        if main_command == 'Stop':
            print(print_pieces(data))
            break

        if main_command == 'Add':
            add_pieces(command[1], command[2], command[3], data)

        elif main_command == 'Remove':
            remove_pieces(command[1], data)

        elif main_command == "ChangeKey":
            changekey(command[1], command[2], data)

number_of_pieces = int(input())
pianist_func(number_of_pieces)

