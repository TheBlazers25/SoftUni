def shopping_list(budget, **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'

    result = []

    for item, (price, quantity) in kwargs.items():
        if len(result) != 5:
            current_item_price = price * quantity
            if current_item_price < budget:
                budget -= current_item_price
                result.append(f'You bought {item} for {current_item_price:.2f} leva.')

    return '\n'.join(result)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
