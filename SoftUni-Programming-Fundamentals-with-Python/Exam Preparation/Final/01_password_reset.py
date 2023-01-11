data = input()

while True:
    command = input().split()
    current_command = command[0]

    if current_command == "Done":
        print(f'Your password is: {data}')
        break

    if current_command == "TakeOdd":
        data = data[1::2]
        print(data)

    if current_command == "Cut":
        index, length = int(command[1]), int(command[2])
        data = data[:index] + data[index + length:]
        print(data)

    if current_command == "Substitute":
        substring, replacement = command[1], command[2]
        if substring in data:
            data = data.replace(substring, replacement)
            print(data)
        else:
            print('Nothing to replace!')