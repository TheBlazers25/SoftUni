number_of_wagons = int(input())
wagons = [0] * number_of_wagons


while True:
    command = input()

    if command == 'End':
        break

    current_command = command.split(' ')

    if current_command[0] == 'add':
        wagons[-1] += int(current_command[-1])
    if current_command[0] == 'insert':
        wagons[int(current_command[1])] += int(current_command[-1])
    if current_command[0] == 'leave':
        wagons[int(current_command[1])] -= int(current_command[-1])

print(wagons)

