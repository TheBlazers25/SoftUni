import re

regex = (r"(?!_)._([a-zA-Z0-9]+)(?!_)")
text_input = input()
x = re.findall(regex, text_input)
print(",".join(x))