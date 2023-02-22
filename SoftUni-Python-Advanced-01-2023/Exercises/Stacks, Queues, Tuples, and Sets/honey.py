from collections import deque

working_bees = deque(int(n) for n in input().split())
nectar = [int(n) for n in input().split()]
symbols = deque(input().split())

honey_made = 0
operators = {
    "+": lambda f, s: f + s,
    "-": lambda f, s: f - s,
    "*": lambda f, s: f * s,
    "/": lambda f, s: f / s
}

while working_bees and nectar:
    current_working_bees = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_working_bees > current_nectar:
        working_bees.appendleft(current_working_bees)
        continue
    symbol = symbols.popleft()

    if current_nectar > 0:
        honey_made += abs(operators[symbol](current_working_bees, current_nectar))

print(f"Total honey made: {honey_made}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

