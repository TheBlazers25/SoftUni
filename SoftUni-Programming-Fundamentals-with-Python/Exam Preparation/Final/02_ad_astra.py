import re

data = input()
pattern = r'(\#|\|)([a-z A-Z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
result = re.findall(pattern, data)

all_foods = ''
days = 0

for foods in result:
    all_foods += f"Item: {foods[1]}, Best before: {foods[2]}, Nutrition: {foods[3]}\n"
    days += int(foods[-1])

number_of_days = int(days / 2000)
print(f'You have food to last you for: {number_of_days} days!')
print(all_foods)


# import re
#
# data = input()
# pattern = r'(\#|\|)([a-z A-Z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
# result = re.findall(pattern, data)
# print_result = ''
# calories = 0
#
# for elements in result:
#     print_result += f"Item: {elements[1]}, Best before: {elements[2]}, Nutrition: {elements[3]}\n"
#     calories += int(elements[-1])
#
# number_of_days = int(calories / 2000)
# print(f"You have food to last you for: {number_of_days} days!")
# print(print_result)