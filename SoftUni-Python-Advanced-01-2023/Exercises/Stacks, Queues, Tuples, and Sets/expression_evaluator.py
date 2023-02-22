from collections import deque

expression = input().split()
numbers = deque()

for element in expression:
    if element in '+-*/':
        while len(numbers) > 1:
            number_one = numbers.popleft()
            number_two = numbers.popleft()

            result = 0

            if element == '+':
                result = number_one + number_two

            elif element == '-':
                result = number_one - number_two

            elif element == '*':
                result = number_one * number_two

            elif element == '/':
                result = number_one // number_two

            numbers.appendleft(result)

    else:
        numbers.append(int(element))

print(numbers.popleft())
