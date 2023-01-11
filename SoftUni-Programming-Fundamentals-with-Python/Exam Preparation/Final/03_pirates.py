data = {}

city = input()
while city != "Sail":
    city_name, population, gold = city.split("||")
    data[city_name] = data.get(city_name, [0, 0])
    data[city_name][0] += int(population)
    data[city_name][1] += int(gold)
    city = input()


def plunder_func(city_name, population, gold, data):
    data[city_name][0] -= int(population)
    data[city_name][1] -= int(gold)
    print(f'{city_name} plundered! {gold} gold stolen, {population} citizens killed.')
    if data[city_name][0] <= 0 or data[city_name][1] <= 0:
        print(f"{city_name} has been wiped off the map!")
        del data[city_name]


def prosper_func(city_name, gold, data):
    if int(gold) > 0:
        data[city_name][1] += int(gold)
        print(f"{gold} gold added to the city treasury. {city_name} now has {data[city_name][1]} gold.")
    else:
        print('Gold added cannot be a negative number!')


def print_func(data):
    if len(data) > 0:
        print(f'Ahoy, Captain! There are {len(data)} wealthy settlements to go to:')
        for city_name in data:
            print(f"{city_name} -> Population: {data[city_name][0]} citizens, Gold: {data[city_name][1]} kg")
    else:
        print('Ahoy, Captain! All targets have been plundered and destroyed!')


while True:
    command = input().split("=>")

    if command[0] == "End":
            print_func(data)
            break

    if command[0] == "Plunder":
        plunder_func(command[1], command[2], command[3], data)

    if command[0] == "Prosper":
        prosper_func(command[1], command[2], data)

