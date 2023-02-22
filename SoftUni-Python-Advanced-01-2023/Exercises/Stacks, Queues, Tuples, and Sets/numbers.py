first_set = set([int(n) for n in input().split()])
second_set = set([int(n) for n in input().split()])

number_of_commands = int(input())

for i in range(number_of_commands):
    command = input()
    numbers = [int(n) for n in command.split() if n.isdigit()]

    if 'Check Subset' in command:
        print(first_set > second_set)

    if 'First' in command:
        if 'Add' in command:
            for number in numbers:
                first_set.add(number)

        if 'Remove' in command:
            for number in numbers:
                if number in first_set:
                    first_set.discard(number)
            # if number in first_set:
            #     first_set.remove(number)
            # else:
            #     continue

    if 'Second' in command:
        if 'Add' in command:
            for number in numbers:
                second_set.add(number)

        if 'Remove' in command:
            for number in numbers:
                if number in second_set:
                    second_set.discard(number)
                # if number in second_set:
                #     second_set.remove(number)
                # else:
                #     continue


print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
