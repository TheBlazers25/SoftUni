orders = {}
product = input().split()

while len(product) > 1:
    name, price, quality = product[0], product[1], product[2]
    if name not in orders.keys():
        orders[name] = []
    orders[name].append(price)
    orders[name].append(quality)
    product = input().split()

print(orders)

for quality in orders.values():
    print(quality)
