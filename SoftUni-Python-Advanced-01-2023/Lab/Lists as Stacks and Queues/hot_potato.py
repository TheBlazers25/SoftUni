from collections import deque

people_deque = deque()

water_amount = int(input())

while True:
    name = input()
    if name == 'Start':
        break
    people_deque.append(name)

command = input()

while command != 'End':

    if 'refill' in command:
        split_command = command.split(' ')
        water_amount += int(split_command[1])

    else:
        liters = int(command)
        if liters <= water_amount:
            print(f'{people_deque.popleft()} got water')
            water_amount -= liters
        else:
            print(f'{people_deque.popleft()} must wait')
    command = input()

print(f'{water_amount} liters left')