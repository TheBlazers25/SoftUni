text = tuple(input())
text_dictionary = {}

for character in text:
    if character not in text_dictionary:
        text_dictionary[character] = 0

    text_dictionary[character] += 1
for key, value in sorted(text_dictionary.items()):
    print(f'{key}: {value} time/s')