import re

number_of_passwords = int(input())

pattern = re.compile(r'(.+)\>(?P<found_pass>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3}))\<\1')

for password_input in range(number_of_passwords):
    password = input()
    find_result = re.finditer(pattern, password)
    found = False
    for show in find_result:
        found = True
        result_print = ''.join(x for x in show["found_pass"] if x)
        if result_print:
            print(f"Password: {result_print.replace('|', '')}")
    if not found:
        print("Try another password!")