initial_arrays = [int(x) for x in input().split()]

while True:
    command = input()

    if command == 'end':
        break

    current_command = command.split(' ')


    if current_command[0] == 'swap':
        initial_arrays[int(current_command[1])], initial_arrays[int(current_command[2])] = initial_arrays[int(current_command[2])], initial_arrays[int(current_command[1])]


    if current_command[0] == 'multiply':
        initial_arrays[int(current_command[1])] *= initial_arrays[int(current_command[2])]


    if current_command[0] == 'decrease':
        initial_arrays = [x - 1 for x in initial_arrays]
        #
        # OR
        # for i in range(len(initial_arrays)):
        # initial_arrays[i] -= 1
        #


print(*initial_arrays, sep=', ')