shopping_list = input().split('!')

while True:
    command = input()

    if command == 'Go Shopping!':
        break

    split_command = command.split()

    if split_command[0] == 'Urgent' and split_command[1] not in shopping_list:
        shopping_list.insert(0, split_command[1])

    if split_command[0] == 'Unnecessary' and split_command[1] in shopping_list:
        shopping_list.remove(split_command[1])

    if split_command[0] == 'Correct':
        for i in range(len(shopping_list)):
            if shopping_list[i] == split_command[1]:
                shopping_list[i] = split_command[2]

    if split_command[0] == 'Rearrange' and split_command[1] in shopping_list:
        shopping_list.remove(split_command[1])
        shopping_list.append(split_command[1])


print(*shopping_list, sep=', ')