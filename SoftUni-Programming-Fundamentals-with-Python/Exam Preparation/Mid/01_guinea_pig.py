quantity_of_food_in_grams = float(input()) * 1000
quantity_of_hay_in_grams = float(input()) * 1000
quantity_of_cover_in_grams = float(input()) * 1000
puppys_weight_in_grams = float(input()) * 1000

for days in range(1, 31):
    quantity_of_food_in_grams -= 300

    if days % 2 == 0:
        quantity_of_hay_in_grams -= quantity_of_food_in_grams * 0.05

    if days % 3 == 0:
        quantity_of_cover_in_grams -= puppys_weight_in_grams / 3

if quantity_of_food_in_grams > 0 and quantity_of_hay_in_grams > 0 and quantity_of_cover_in_grams > 0:
    print(f'Everything is fine! Puppy is happy! Food: {quantity_of_food_in_grams / 1000:.2f}, Hay: {quantity_of_hay_in_grams / 1000:.2f}, Cover: {quantity_of_cover_in_grams / 1000:.2f}.')
else:
    print("Merry must go to the pet store!")