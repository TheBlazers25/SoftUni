from collections import deque


def gifts(value):
    if 199 > value > 100:
        materials.pop()
        magic_level.popleft()

    elif 299 > value > 200:
        materials.pop()
        magic_level.popleft()

    elif 399 > value > 300:
        materials.pop()
        magic_level.popleft()
    elif 499 > value > 400:
        materials.pop()
        magic_level.popleft()


materials = [int(n) for n in input().split()]
magic_level = deque(int(n) for n in input().split())

gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0

wedding = False

while True:

    if gemstone > 0 and porcelain_sculpture > 0 or gold > 0 and diamond_jewellery > 0:
        wedding = True

    if not materials:
        break

    if not magic_level:
        break

    product_of_operations = materials[-1] + magic_level[0]

    if product_of_operations < 100:
        if product_of_operations % 2 == 0:
            materials[-1] *= 2
            magic_level[0] *= 3
            new_value = materials[-1] + magic_level[0]

        elif product_of_operations % 2 != 0:
            materials[-1] *= 2
            magic_level[0] *= 2
            new_value = materials[-1] + magic_level[0]

        if new_value < 100:
            materials.pop()
            magic_level.popleft()

    elif product_of_operations > 499:
        product_of_operations /= 2
        if 499 > product_of_operations > 100:
            if 199 > product_of_operations > 100:
                gemstone += 1
                materials.pop()
                magic_level.popleft()

            elif 299 > product_of_operations > 200:
                porcelain_sculpture += 1
                materials.pop()
                magic_level.popleft()

            elif 399 > product_of_operations > 300:
                gold += 1
                materials.pop()
                magic_level.popleft()
            elif 499 > product_of_operations > 400:
                diamond_jewellery += 1
                materials.pop()
                magic_level.popleft()

    elif 199 > product_of_operations > 100:
        gemstone += 1
        materials.pop()
        magic_level.popleft()
    elif 299 > product_of_operations > 200:
        porcelain_sculpture += 1
        materials.pop()
        magic_level.popleft()
    elif 399 > product_of_operations > 300:
        gold += 1
        materials.pop()
        magic_level.popleft()
    elif 499 > product_of_operations > 400:
        diamond_jewellery += 1
        materials.pop()
        magic_level.popleft()

if wedding:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')


if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
if magic_level:
    print(f'Magic left: {", ".join(map(str, magic_level))}')

if gemstone:
    print(f'Gemstone: {gemstone}')
if porcelain_sculpture:
    print(f'Porcelain Sculpture: {porcelain_sculpture}')
if gold:
    print(f'Gold: {gold}')
if diamond_jewellery:
    print(f'Diamond jewellery: {diamond_jewellery}')
