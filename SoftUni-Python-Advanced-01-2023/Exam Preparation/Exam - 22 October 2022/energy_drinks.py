from collections import deque

mg_of_caffeine = [int(n) for n in input().split(', ')]
energy_drinks = deque(int(n) for n in input().split(', '))

maximum_caffeine = 0

while True:
    if not mg_of_caffeine:
        break

    if not energy_drinks:
        break

    current_mg_of_caffeine = mg_of_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    current_caffeine = current_mg_of_caffeine * current_energy_drink

    if maximum_caffeine + current_caffeine <= 300:
        maximum_caffeine += current_caffeine

    else:
        maximum_caffeine -= 30
        if maximum_caffeine < 0:
            maximum_caffeine = 0
        energy_drinks.append(current_energy_drink)

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {maximum_caffeine} mg caffeine.")
