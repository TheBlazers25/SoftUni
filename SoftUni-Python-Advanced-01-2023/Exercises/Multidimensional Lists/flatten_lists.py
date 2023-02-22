elements = input().split('|')[::-1]

for element in range(len(elements)):
    for num in elements[element].split():
        print(num, end=' ')
