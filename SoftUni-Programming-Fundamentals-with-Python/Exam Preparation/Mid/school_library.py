bookshelf = input().split("&")

while True:
    command = input()

    if command == "Done":
        break

    split_command = command.split(" | ")

    if split_command[0] == 'Add Book' and split_command[1] not in bookshelf:
        bookshelf.insert(0, split_command[1])

    if split_command[0] == 'Take Book' and split_command[1] in bookshelf:
        bookshelf.remove(split_command[1])

    if split_command[0] == 'Swap Books' and split_command[1] in bookshelf and split_command[2] in bookshelf:
        first_index, second_index = bookshelf.index(split_command[1]), bookshelf.index(split_command[2])
        bookshelf[first_index], bookshelf[second_index] = bookshelf[second_index], bookshelf[first_index]

    if split_command[0] == 'Insert Book' and split_command[1] not in bookshelf:
        bookshelf.append(split_command[1])

    if split_command[0] == 'Check Book' and int(split_command[1]) <= len(bookshelf):
        print(bookshelf[int(split_command[1])])

print(*bookshelf , sep=', ')