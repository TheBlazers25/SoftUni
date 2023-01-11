data = {}
areas = {}

command = input()

while command != 'EndDay':
    command_type, animal_info = command.split(": ")
    command = input()

    if command_type == 'Add':
        animal_name, food, area = animal_info.split("-")
        food = int(food)

        if animal_name not in data:
            data[animal_name] = food
            if area not in areas:
                areas[area] = 1
            else:
                areas[area] += 1
        else:
            data[animal_name] += food

    if command_type == 'Feed':
        animal_name, food = animal_info.split("-")
        food = int(food)

        if animal_name in data:
            data[animal_name] -= food

            if data[animal_name] <= 0:
                print(f'{animal_name} was successfully fed')
                del data[animal_name]
                areas[area] -= 1

                if areas[area] <= 0:
                    del areas[area]

print('Animals:')
for animal_name in data:
    print(f' {animal_name} -> {data[animal_name]}g')

print('Areas with hungry animals:')
for area in areas:
    print(f' {area}: {areas[area]}')



