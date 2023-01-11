vehicles = input().split(">>")

tax_collected = 0

for cars in vehicles:
    current_taxes = 0

    car_type, years, kilometers = [int(x) if x.isdigit() else x for x in cars.split()]

    if car_type == 'family' or car_type == 'heavyDuty' or car_type == 'sports':

        if car_type == 'family':
            current_taxes = 50  + (int(kilometers / 3000) * 12) - (5 * years)
            tax_collected += current_taxes
            print(f"A {car_type} car will pay {current_taxes:.2f} euros in taxes.")

        if car_type == 'heavyDuty':
            current_taxes = 80 + (int(kilometers / 9000) * 14) - (8 * years)
            tax_collected += current_taxes
            print(f"A {car_type} car will pay {current_taxes:.2f} euros in taxes.")

        if car_type == 'sports':
            current_taxes = 100 + (int(kilometers / 2000) * 18) - (9 * years)
            tax_collected += current_taxes
            print(f"A {car_type} car will pay {current_taxes:.2f} euros in taxes.")

    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {tax_collected:.2f} euros in taxes.")

#Formatting the code