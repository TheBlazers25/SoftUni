number_of_lines = int(input())
counter = 0
for lines in range(number_of_lines):
    letter = str(input())
    counter  += ord(letter)
print(f"The sum equals: {counter}")
