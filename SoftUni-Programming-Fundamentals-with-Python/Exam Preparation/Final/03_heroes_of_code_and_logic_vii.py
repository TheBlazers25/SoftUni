def store_heroes(number):
    data = {}

    for _ in range(number):
        hero_stats = input().split(' ')
        hero_name, hp, mp = hero_stats[0], int(hero_stats[1]), int(hero_stats[2])
        data[hero_name] = [hp, mp]

    return data


def cast_spell_func(hero_name, mp_needed, spell_name, data):
    if data[hero_name][1] >= mp_needed:
        data[hero_name][1] -= mp_needed
        print(f'{hero_name} has successfully cast {spell_name} and now has {data[hero_name][1]} MP!')
    else:
        print(f'{hero_name} does not have enough MP to cast {spell_name}!')


def take_damage_func(hero_name, damage, attacker, data):
    if data[hero_name][0] > damage:
        data[hero_name][0] -= damage
        print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {data[hero_name][0]} HP left!')
    else:
        print(f'{hero_name} has been killed by {attacker}!')
        del data[hero_name]


def recharge_func(hero_name, amount, data):
    leftover_mana = 200 - data[hero_name][1]
    data[hero_name][1] += amount
    if data[hero_name][1] > 200:
        data[hero_name][1] = 200
        print(f'{hero_name} recharged for {leftover_mana} MP!')
    else:
        print(f'{hero_name} recharged for {amount} MP!')


def heal_func(hero_name, amount, data):
    leftover_hp = 100 - data[hero_name][0]
    data[hero_name][0] += amount
    if data[hero_name][0] > 100:
        data[hero_name][0] = 100
        print(f'{hero_name} healed for {leftover_hp} HP!')
    else:
        print(f'{hero_name} healed for {amount} HP!')


def print_heroes_func(data):
    for hero_name in data:
        print(f'{hero_name}\n  HP: {data[hero_name][0]}\n  MP: {data[hero_name][1]}')


def heroes_func(number):

    data = store_heroes(number)

    while True:
        command = input().split(' - ')

        if command[0] == 'End':
            print_heroes_func(data)
            break

        if command[0] == 'CastSpell':
            cast_spell_func(command[1], int(command[2]), command[3], data)

        if command[0] == 'TakeDamage':
            take_damage_func(command[1], int(command[2]), command[3], data)

        if command[0] == 'Recharge':
            recharge_func(command[1], int(command[2]), data)

        if command[0] == 'Heal':
            heal_func(command[1], int(command[2]), data)

number_of_heroes = int(input())
heroes_func(number_of_heroes)
