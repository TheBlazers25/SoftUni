string_input = input()
parenthesis = []

for i in range(len(string_input)):
    if string_input[i] == '(':
        parenthesis.append(i)
    elif string_input[i] == ')':
        first_index = parenthesis.pop()
        print(string_input[first_index:i + 1])