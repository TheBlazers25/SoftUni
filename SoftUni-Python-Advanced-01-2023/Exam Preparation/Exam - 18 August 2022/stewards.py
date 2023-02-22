from collections import deque

seats = input().split(', ')
first_sequence = deque(int(n) for n in input().split(', '))
second_sequence = [int(n) for n in input().split(', ')]

rotations = 0
seat_matches_counter = 0
seat_matches = []

while True:

    if seat_matches_counter == 3 or rotations == 10:
        print(f'Seat matches: {", ".join(seat_matches)}')
        print(f'Rotations count: {rotations}')
        break

    first_sequence_number = first_sequence.popleft()
    second_sequence_number = second_sequence.pop()
    sum_of_sequence_number = first_sequence_number + second_sequence_number
    ascii_value = chr(sum_of_sequence_number)

    check_first_seat = str(first_sequence_number) + ascii_value
    check_second_seat = str(second_sequence_number) + ascii_value

    if check_first_seat in seats:
        seat_matches.append(check_first_seat)
        seats.remove(check_first_seat)
        seat_matches_counter += 1
        rotations += 1

    elif check_second_seat in seats:
        seat_matches.append(check_second_seat)
        seats.remove(check_second_seat)
        seat_matches_counter += 1
        rotations += 1

    else:
        first_sequence.append(first_sequence_number)
        second_sequence.insert(0, second_sequence_number)
        rotations += 1

    # for seat in [check_first_seat, check_second_seat]:
    #     if seat in seat_matches:
    #         break
    #     if seat in seats:
    #         seats.remove(seat)
    #         seat_matches.append(seat)
    #         break
    # else:
    #     first_sequence.append(first_sequence_number)
    #     second_sequence.insert(0, second_sequence_number)
    # rotations += 1
