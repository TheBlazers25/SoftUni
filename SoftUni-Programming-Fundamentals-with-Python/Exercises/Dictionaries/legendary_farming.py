items_dictionary = {"shards": 0, "fragments": 0, "motes": 0}
items = input().split()
obtained = False

while not obtained:
    for index in range(0, len(items), 2):
        value = int(items[index])
        key = items[index+ 1].lower()
        if key not in items_dictionary.keys():
            items_dictionary[key] = 0
        items_dictionary[key] += value

        if items_dictionary['shards'] >= 250:
            print("Shadowmourne  obtained!")
            items_dictionary['shards'] -= 250
            obtained = True

        elif items_dictionary['fragments'] >= 250:
            print("Valanyr obtained!")
            items_dictionary['fragments'] -= 250
            obtained = True

        elif items_dictionary['motes'] >= 250:
            print("Dragonwrath obtained!")
            items_dictionary['motes'] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    items = input().split()

for material, quantity in items_dictionary.items():
    print(f"{material}: {quantity}")