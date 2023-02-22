def grocery_store(**kwargs):
    result = ''
    receipt = {}

    for product_name, product_quantity in kwargs.items():
        receipt[product_name] = product_quantity

    sorted_dict = dict(sorted(receipt.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    for key, value in sorted_dict.items():
        result += f'{key}: {value}\n'
    return result

print(grocery_store(
bread=5,
pasta=12,
eggs=12,
))