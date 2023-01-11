data = input()

while True:
    command = input().split('>>>')
    current_command = command[0]

    if current_command == 'Generate':
        print(f'Your activation key is: {data}')
        break

    if current_command == 'Contains':
        substring = command[1]
        if substring in data:
            print(f'{data} contains {substring}')
        else:
            print('Substring not found!')

    if current_command == 'Flip':
        start_index, end_index = int(command[2]), int(command[3])
        if command[1] == 'Upper':
            upper_substring = data[start_index:end_index].upper()
            data = data[:start_index] + upper_substring + data[end_index:]
            print(data)
        else:
            if command[1] == 'Lower':
                lower_substring = data[start_index:end_index].lower()
                data = data[:start_index] + lower_substring + data[end_index:]
                print(data)

    if current_command == 'Slice':
        index, length = int(command[1]), int(command[2])
        data = data[:index] + data[length:]
        print(data)
