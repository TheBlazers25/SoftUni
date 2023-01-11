resources = input()

resources_dictionary = {}

while resources != "stop":
    quantity = int(input())
    key = resources
    value = quantity
    if key not in resources_dictionary.keys():
        resources_dictionary[key] = 0
    resources_dictionary[key] += value
    resources = input()

for key, value in resources_dictionary.items():
    print(f"{key} -> {value}")





