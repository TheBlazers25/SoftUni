number_of_rooms = int(input())
chairs_left_counter = 0
chairs_needed_counter = 0

for rooms in range(number_of_rooms):
    room = input().split(' ')
    if len(room[0]) >= int(room[1]):
        chairs_left = len(room[0]) - int(room[1])
        chairs_left_counter += 1
    else:
        chairs_needed_counter += 1
        print(f'{chairs_needed_counter} more chairs needed in room {rooms + 1}')

if chairs_left_counter > 0 and chairs_needed_counter == 0:
    print(f"Game On, {chairs_left_counter} free chairs left")