number_of_guests = int(input())

guests = []

for i in range(number_of_guests):
    reservation_code = input()
    guests.append(reservation_code)

while True:
    guests_who_came = input()

    if guests_who_came == 'END':
        break

    if guests_who_came in guests:
        guests.remove(guests_who_came)

sorted_guests = sorted(guests)

print(len(guests))
print(*sorted_guests, sep='\n')
