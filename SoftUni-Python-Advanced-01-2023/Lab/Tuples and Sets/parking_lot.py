number_of_commands = int(input())
parking_lot = set()

COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

for _ in range(number_of_commands):
    command, car_number = input().split(', ')

    if command == COMMAND_IN:
        parking_lot.add(car_number)

    elif command == COMMAND_OUT:
        parking_lot.remove(car_number)

if len(parking_lot) > 0:
    print(*parking_lot, sep='\n')

else:
    print('Parking Lot is Empty')


