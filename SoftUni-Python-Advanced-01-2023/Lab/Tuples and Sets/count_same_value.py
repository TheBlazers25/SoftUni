numbers = input().split(' ')
numbers_dictionary = {}

for number in numbers:
    if number not in numbers_dictionary:
        numbers_dictionary[number] = 0

    numbers_dictionary[number] += 1

for key, value in numbers_dictionary.items():
    key = float(key)
    print(f"{key} - {value} times")


# values = tuple(map(float, input().split(' ')))
# values_counter = {}
# 
# for value in values:
#     if value not in values_counter:
#         values_counter[value] = 0
#     values_counter[value] += 1
#
# for k, v in values_counter.items():
#     print(f'{k} - {v} times')