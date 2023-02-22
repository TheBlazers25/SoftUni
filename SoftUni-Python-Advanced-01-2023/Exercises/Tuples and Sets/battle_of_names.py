number_of_names = int(input())

odd_set = set()
even_set = set()


for row in range(1, number_of_names + 1):
    name = tuple(input())
    current_name_value = 0

    for character in name:
        current_name_value += ord(character)

    divided_value = int(current_name_value/row)

    if divided_value % 2 != 0:
        odd_set.add(divided_value)

    else:
        even_set.add(divided_value)

if sum(odd_set) > sum(even_set):
    print(*odd_set - even_set, sep=', ')

elif sum(even_set) > sum(odd_set):
    print(*even_set ^ odd_set, sep=', ')

else:
    print(*odd_set ^ even_set, sep=', ')
