numbers = input()


def all_sum(num):
    return f"Odd sum = {sum(int(n) for n in num if int(n) % 2 != 0)}," \
           f" Even sum = {sum(int(n) for n in num if int(n) % 2 ==0)}"


print(all_sum(numbers))