data = input()

while True:
    command = input().split(':')
    current_command = command[0]

    if current_command == 'Travel':
        print(f'Ready for world tour! Planned stops: {data}')
        break

    elif current_command == 'Add Stop':
        index, string = int(command[1]), command[2]
        if 0 <= index < len(data):
            data = data[:index] + string + data[index:]
        print(data)

    elif current_command == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index < len(data) and 0 <= end_index < len(data):
            data = data[:start_index] + data[(end_index+1):]
        print(data)

    elif current_command == 'Switch':
        old_string, new_string = command[1], command[2]
        if old_string in data:
            data = data.replace(old_string, new_string)
        print(data)