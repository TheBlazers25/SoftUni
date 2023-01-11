numbers = [int(x) for x in input().split()]

result = sorted([x for x in numbers if x > sum(numbers)/len(numbers)]) # or add ",reverse=True" at the end

if result:
    print(*result[-5:][-1::-1])
else:
    print("No")