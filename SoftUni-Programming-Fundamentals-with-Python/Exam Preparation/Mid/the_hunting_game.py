days_of_adventure = int(input())
number_of_players = int(input())
energy = float(input())
water_per_day = float(input())
food_per_day = float(input())

total_water = days_of_adventure * number_of_players * water_per_day
total_food = days_of_adventure * number_of_players * food_per_day


for days in range(1, days_of_adventure + 1):
    energy_lost = float(input())

    energy -= energy_lost

    if energy <= 0:
        print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')
        break

    if days % 2 == 0:
        total_water = total_water - (total_water * 0.3)
        energy = energy + (energy * 0.05)

    if days % 3 == 0:
        total_food = total_food - (total_food / number_of_players)
        energy = energy + (energy * 0.10)

if energy > 0:
    print(f'You are ready for the quest. You will be left with - {energy:.2f} energy!')