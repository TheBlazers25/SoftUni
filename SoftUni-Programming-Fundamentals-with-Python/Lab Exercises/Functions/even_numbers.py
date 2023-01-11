def even_filter(number):
    return number % 2 == 0

enter_numbers = [int(n) for n in input().split()]
filtered_list = list(filter(even_filter, enter_numbers))
print(filtered_list)
