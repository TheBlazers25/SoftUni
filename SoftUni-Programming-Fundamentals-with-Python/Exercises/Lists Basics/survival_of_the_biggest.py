numbers = input().split()
list_of_numbers = []

for element in numbers:
    list_of_numbers.append(int(element))

count_to_remove = int(input())

for count in range(count_to_remove):
    list_of_numbers.remove(min(list_of_numbers))
res = str (list_of_numbers) [ 1 : - 1 ]
print(res)