given_string_list = list(input())
reversed_string_list = []

while given_string_list:
    reversed_string_list.append(given_string_list.pop())

print("".join(reversed_string_list))

# given_string_list = list(input())
#
# while given_string_list:
#     reversed = given_string_list.pop()
#     print(reversed, end='')