countries = input().split(', ')
capital_cities = input().split(', ')

dictionary = dict(zip(countries, capital_cities))

for key, value in dictionary.items():
    print(f"{key} -> {value}")