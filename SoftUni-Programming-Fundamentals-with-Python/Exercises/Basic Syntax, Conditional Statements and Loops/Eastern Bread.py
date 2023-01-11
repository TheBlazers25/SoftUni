budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price = flour_price * 1.25
price_for_the_milk_used = milk_price / 4

loaf_price = flour_price + egg_price + price_for_the_milk_used
while loaf_price > budget:
    pass
else:
    pass
#"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."