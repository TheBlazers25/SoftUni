import re

data = input()
pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'
result = re.findall(pattern, data)

emoji_counter = 0
cool = 1

all_digits = "".join(x for x in data if x .isdigit())
for num in all_digits:
    cool *= int(num)

print(f'Cool threshold: {cool}')

for emojis in result:
    emoji_counter +=1

print(f'{emoji_counter} emojis found in the text. The cool ones are:')

for found in result:
    find_cool = 0
    for letter in found[1]:
        find_cool += ord(letter)
    if find_cool >= cool:
        print(f'{found[0]}{found[1]}{found[0]}')