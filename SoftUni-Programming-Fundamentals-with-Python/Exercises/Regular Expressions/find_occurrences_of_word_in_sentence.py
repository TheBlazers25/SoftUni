import re

regex = (r"(?!_)._([a-zA-Z0-9]+)(?!_)")
text_input = input()
searched_word = input()

x = re.findall(searched_word, text_input)
print(",".join(x))