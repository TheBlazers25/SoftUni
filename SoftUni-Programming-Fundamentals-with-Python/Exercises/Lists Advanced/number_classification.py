numbers = [int(n) for n in input().split(', ')]

possitive_check = [num for num in numbers if num >= 0]
print('Positive:', end=' ')
print(*possitive_check, sep=', ')

negative_check = [num for num in numbers if num < 0]
print('Negative:', end=' ')
print(*negative_check, sep=', ')

even_check  = [num for num in numbers if num % 2 == 0]
print('Even:', end=' ')
print(*even_check, sep=', ')

odd_check  = [num for num in numbers if num % 2 != 0]
print('Odd:', end=' ')
print(*odd_check, sep=', ')

