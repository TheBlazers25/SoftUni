import re

data = input()
pattern = r'(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'
result = re.findall(pattern, data)

counter = 0
word_list = []

# for pairs in result:
#     if pairs[1] == pairs[3][::-1]:
#         word_list.append(f'{pairs[1]} <=> {pairs[3]}')
#     counter += 1
#
# if counter > 0:
#     print(f'{counter} word pairs found!')
#
#     if not word_list:
#         print('No mirror words')
#     else:
#         print(f'The mirror words are:\n{", ".join(word_list)}')
#
# else:
#     print('No word pairs found')
#     print('No mirror words')

