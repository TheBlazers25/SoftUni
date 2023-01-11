def store_plants_func(number):
    data = {}

    for _ in range(number):
        plant_data = input().split("<->")
        plant_name, rarity = plant_data[0], int(plant_data[1])
        data[plant_name] = [rarity, []]

    return data


def rate_plants_func(plant_name, rating, data):
    if plant_name in data:
        data[plant_name][1].append(int(rating))
    else:
        print("error")


def update_plants_func(plant_name, new_rarity, data):
    if plant_name in data:
        data[plant_name][0] = new_rarity
    else:
        print("error")


def reset_plant_func(plant_name, data):
    if plant_name in data:
        data[plant_name][1] = []
    else:
        print("error")


def print_plant_func(data):
    result = ''
    print('Plants for the exhibition:')
    for plant_name in data:
        average_rating = 0
        rarity = data[plant_name][0]
        rating = data[plant_name][1]
        if sum(data[plant_name][1]) != 0:
            average_rating = sum(data[plant_name][1]) / len(data[plant_name][1])
        result += f' - {plant_name}; Rarity: {data[plant_name][0]}; Rating: {average_rating:.2f}\n'

    return result


def plant_func(number):

    data = store_plants_func(number)

    while True:
        command = input().split(' ')

        if command[0] == 'Exhibition':
            print(print_plant_func(data))
            break

        if command[0] == 'Rate:':
            rate_plants_func(command[1], command[3], data)

        if command[0] == 'Update:':
            update_plants_func(command[1], command[3], data)

        if command[0] == 'Reset:':
            reset_plant_func(command[1], data)


number_of_plants = int(input())
plant_func(number_of_plants)
