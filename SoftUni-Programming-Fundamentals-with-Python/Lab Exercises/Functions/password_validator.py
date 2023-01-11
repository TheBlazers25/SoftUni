input_password = input()
only_letters_and_digits = False
password_in_range = False
check_length = False
check_number_length = 0

if 6 <= len(input_password) <= 10:
    password_in_range = True
else:
    print("Password must be between 6 and 10 characters")

if input_password.isalnum():
    only_letters_and_digits = True
else:
    print("Password must consist only of letters and digits")


for number in input_password:
    if number.isdigit():
        check_number_length += 1
    if check_number_length == 2:
        check_length = True
        break

if check_length == False:
    print("Password must have at least 2 digits")


if input_password.isalnum() and password_in_range == True and check_length == True:
    print("Password is valid")
# number = input()
# check_number = 0
# two_numbers = False
#
# for numbers in number:
#     if number.isdigit():
#         check_number += 1
#     if check_number == 2:
#         two_numbers = True
#
# if two_numbers == True:
#     print("GG")
# else:
#     print("Fail")