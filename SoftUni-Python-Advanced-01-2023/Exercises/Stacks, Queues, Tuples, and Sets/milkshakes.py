from collections import deque

chocolate = [int(n) for n in input().split(', ')]
cups_of_milk = deque([int(n) for n in input().split(', ')])

milkshakes = 0

while chocolate and cups_of_milk and milkshakes != 5:
    current_chocolate = chocolate.pop()
    current_cups_of_milk = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_cups_of_milk <= 0:
        continue

    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cups_of_milk)
        continue

    elif current_cups_of_milk <= 0:
        chocolate.append(current_chocolate)
        continue

    if current_chocolate == current_cups_of_milk:
        milkshakes += 1
        continue

    else:
        cups_of_milk.append(current_cups_of_milk)
        chocolate.append(current_chocolate - 5)


if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print('Chocolate: empty')

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print('Milk: empty')
