# numbers = [int(n) for n in input().split()]
#
# positive_sum = 0
# negative_sum = 0
#
# for number in numbers:
#     if number > 0:
#         positive_sum += number
#
#     if number < 0:
#         negative_sum += number
#
# print(negative_sum)
# print(positive_sum)
#
# if positive_sum > abs(negative_sum):
#     print("The positives are stronger than the negatives")
# else:
#     print("The negatives are stronger than the positives")


def check_number(numbers):
    positive_sum = 0
    negative_sum = 0

    for number in numbers:
        if number > 0:
            positive_sum += number

        if number < 0:
            negative_sum += number

    if positive_sum > abs(negative_sum):
        text = "The positives are stronger than the negatives"
    else:
        text = "The negatives are stronger than the positives"

    return f"{negative_sum}\n{positive_sum}\n{text}"


numbers = [int(n) for n in input().split()]
print(check_number(numbers))

