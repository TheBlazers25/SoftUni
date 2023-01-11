def car_storage_func(number):
    data = {}

    for _ in range(number):
        car_info = input().split('|')
        car, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])

        data[car] = [mileage, fuel]

    return data


def drive_func(car, distance, fuel_used, data):
    if fuel_used < data[car][1]:
        data[car][0] += distance
        data[car][1] -= fuel_used
        print(f'{car} driven for {distance} kilometers. {fuel_used} liters of fuel consumed.')

    else:
        print('Not enough fuel to make that ride')

    if data[car][0] >= 100000:
        print(f"Time to sell the {car}!")
        del data[car]


def refuel_func(car, added_fuel, data):
    left_over_fuel = 75 - data[car][1]
    data[car][1] += added_fuel
    if data[car][1] > 75:
        data[car][1] = 75
        print(f'{car} refueled with {left_over_fuel} liters')
    else:
        print(f'{car} refueled with {added_fuel} liters')


def revert_func(car, kilometers, data):
    data[car][0] -= kilometers
    if data[car][0] < 10000:
        data[car][0] = 10000
    else:
        print(f'{car} mileage decreased by {kilometers} kilometers')


def print_car_func(data):
    result = ''
    for car in data:
        mileage = data[car][0]
        fuel = data[car][1]
        result += f'{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.\n'

    return result


def car_func(number):

    data = car_storage_func(number)

    while True:
        command = input().split(' : ')
        main_command = command[0]

        if main_command == 'Stop':
            print(print_car_func(data))
            break

        if main_command == 'Drive':
            drive_func(command[1], int(command[2]), int(command[3]), data)

        if main_command == 'Refuel':
            refuel_func(command[1], int(command[2]), data)

        if main_command == 'Revert':
            revert_func(command[1], int(command[2]), data)


number_of_cars = int(input())
car_func(number_of_cars)
