def stock_availability(boxes, *args):
    inventory_list = []

    parameter = args[0]
    other_parameters = args[1:]

    if parameter == 'delivery':
        inventory_list = boxes
        inventory_list += other_parameters

    else:
        inventory_list = boxes
        if not other_parameters:
            inventory_list = boxes[1:]

        elif isinstance(other_parameters[0], int):
            inventory_list = inventory_list[other_parameters[-1]:]

        for item in other_parameters:
            if item in inventory_list:
                while item in inventory_list:
                    inventory_list.remove(item)

    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
