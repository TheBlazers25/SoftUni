def even_odd(*args):
    *numbers, command = args

    even_list = []
    odd_list = []

    for number in numbers:
        if (number % 2) == 0:
            even_list.append(number)

        else:
            odd_list.append(number)

    if command == 'even':
        return even_list

    else:
        return odd_list

print(even_odd(1, 2, 3, 4, 5, 6, "even"))