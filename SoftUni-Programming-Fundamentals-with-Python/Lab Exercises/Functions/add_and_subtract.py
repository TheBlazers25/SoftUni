# def add(first, second):
#     return first_number + second_number
#
# def subtract(sum, third):
#     return sum - third
#
# def add_and_subtract(first, second, third):
#     sum_of_two = add(first, second)
#     result = subtract(sum_of_two, third)
#     return result

def add_and_subtract(first, second, third):
    def add(first, second):
        return first_number + second_number

    def subtract(sum, third):
        return sum - third

    sum_of_two = add(first, second)
    result = subtract(sum_of_two, third)
    return result

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))

# def smallest_number(number1, number2, number3):
#     final_sum = (number1 + number2) - number3
#     print(final_sum)
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
#
# smallest_number(number1, number2, number3)
