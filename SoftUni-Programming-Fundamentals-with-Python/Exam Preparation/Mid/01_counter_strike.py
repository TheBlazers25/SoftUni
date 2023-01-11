initial_energy = int(input())
distance = input()
win_counter = 1

while distance != 'End the battle':
    distance = int(distance)
    initial_energy -= distance

    if initial_energy <= 0:
        print(f'Not enough energy! Game ends with {win_counter} won battles and {initial_energy} energy')
        break

    win_counter += 1
    if win_counter % 3 == 0:
            initial_energy += win_counter

    distance = input()

else:
    print(f'Won battles: {win_counter}. Energy left: {initial_energy}')





# initial_energy = int(input())
# distance = input()
# win_counter = 0
#
# while distance != 'End of battle':
#
#         distance = int(distance)
#         initial_energy -= int(distance)
#
#
#
#         if initial_energy < 0:
#             print(f'Not enough energy! Game ends with {win_counter} won battles and {initial_energy + distance} energy')
#
#         win_counter += 1
#         if win_counter % 3 == 0:
#             initial_energy += win_counter
#
#         distance = input()
#
# else:
#     print(f'Won battles: {win_counter}. Energy left: {initial_energy}')




# initial_energy = int(input())
# distance = input()
# win_counter = 0

# while distance != 'End of battle':
#
#     distance = int(distance)
#     initial_energy -= distance
#
#     if initial_energy < 0:
#         print(f'Not enough energy! Game ends with {win_counter} won battles and {initial_energy + distance} energy')
#         break
#
#     win_counter += 1
#     if win_counter % 3 == 0:
#         initial_energy += win_counter
#
#     distance = input()
#
# else:
#     print(f'Won battles: {win_counter}. Energy left: {initial_energy}')
