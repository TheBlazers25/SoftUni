command = ''
price = 0
tax = 0
final_price = 0


while command != 'special' and command != 'regular':
    command = input()
    try:
        if float(command) >= 0:
            price += float(command)
        else:
            print('Invalid price!')
    except ValueError:
        pass


tax += price * 0.2


if command == 'special':
    final_price = (price + tax) * 0.9
else:
    final_price = price + tax


if price > 0:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {price:.2f}$')
    print(f'Taxes: {tax:.2f}$')
    print('-----------')
    print(f'Total price: {final_price:.2f}$')
else:
    print('Invalid order!')
