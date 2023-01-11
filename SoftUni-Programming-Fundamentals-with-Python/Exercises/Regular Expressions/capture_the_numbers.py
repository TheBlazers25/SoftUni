import re

regex = (r"\d+")
while True:
    text_input = input()
    if text_input:
        x = re.findall(regex, text_input)
        for show in x:
            print(x[0], end=" ")
    else:
        break

# import re
#
# regex = re.compile(r"\d+")
# while True:
#     text_input = input()
#     if text_input:
#         x = regex.finditer(text_input)
#
#         for show in x:
#             print(show[0], end=" ")
#     else:
#         break