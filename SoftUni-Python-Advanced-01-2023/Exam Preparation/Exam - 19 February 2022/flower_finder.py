# from collections import deque
#
# vowels = deque(input().split())
# consonants = input().split()
#
# rose_letters = ['r', 'o', 's', 'e']
# tulip_letters = ['t', 'u', 'l', 'i', 'p']
# lotus_letters = ['l', 'o', 't', 'u', 's']
# daffodil_letters = ['d', 'a', 'f', 'f', 'o', 'd', 'i', 'l']
#
# final_word = ''
#
# while True:
#
#     if not rose_letters or tulip_letters or lotus_letters or daffodil_letters:
#         if len(rose_letters) == 0:
#             final_word += 'rose'
#             break
#         elif len(tulip_letters) == 0:
#             final_word += 'tulip'
#             break
#         elif len(lotus_letters) == 0:
#             final_word += 'lotus'
#             break
#         elif len(daffodil_letters) == 0:
#             final_word += 'daffodil'
#             break
#
#     if not vowels:
#         break
#
#     if not consonants:
#         break
#
#     first_vowel = vowels.popleft()
#     last_consonant = consonants.pop()
#
#     if first_vowel in rose_letters:
#         rose_letters.remove(first_vowel)
#
#     if last_consonant in rose_letters:
#         rose_letters.remove(last_consonant)
#
#     if first_vowel in tulip_letters:
#         tulip_letters.remove(first_vowel)
#
#     if last_consonant in tulip_letters:
#         tulip_letters.remove(last_consonant)
#
#     if first_vowel in lotus_letters:
#         lotus_letters.remove(first_vowel)
#
#     if last_consonant in lotus_letters:
#         lotus_letters.remove(last_consonant)
#
#     while first_vowel in daffodil_letters:
#         daffodil_letters.remove(first_vowel)
#
#     while last_consonant in daffodil_letters:
#         daffodil_letters.remove(last_consonant)
#
# if final_word:
#     print(f'Word found: {final_word}')
# else:
#     print('Cannot find any word!')
#
# if vowels:
#     print(f'Vowels left: {" ".join(vowels)}')
#
# if consonants:
#     print(f'Consonants left: {" ".join(consonants)}')

