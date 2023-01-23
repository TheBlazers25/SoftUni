amount_of_lines = int(input())

queries = []

push_number = '1'
delete_number = '2'
print_max = '3'
print_min = '4'

for i in range(amount_of_lines):
    command = input()

    if command[0] == push_number:
        command_split = command.split(' ')
        queries.append(command_split[1])

    elif command == delete_number:
        if len(queries) != 0:
            queries.pop()
        else:
            pass

    elif command == print_max:
        print(max(queries))

    elif command == print_min:
        print(min(queries))

print(', '.join(queries[::-1]))