data = input()

while True:
    command = input().split(' ')
    current_command = command[0]

    if current_command == 'Abracadabra':
        break

    elif current_command == 'Abjuration':
        data = data.upper()
        print(data)

    elif current_command == 'Necromancy':
        data = data.lower()
        print(data)

    elif current_command == 'Illusion':
        index, letter = int(command[1]), command[2]
        if index + 1 <= len(data):
            data = data[:index] + letter + data[index+ 1:]
            print('Done!')
        else:
            print('The spell was too weak.')

    elif current_command == 'Divination':
        first_substring, second_substring = command[1], command[2]
        if first_substring in data:
            data = data.replace(first_substring, second_substring)
            print(data)

    elif current_command == 'Alteration':
        substring = command[1]
        if substring in data:
            data = data.replace(substring, '')
            print(data)

    else:
        print('The spell did not work!')
