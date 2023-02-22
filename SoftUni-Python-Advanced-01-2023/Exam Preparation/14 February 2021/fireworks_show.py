from collections import deque

firework_effects = deque(int(n) for n in input().split(', '))
explosive_power = [int(n) for n in input().split(', ')]

fireworks = {'Palm': 0, 'Willow': 0, 'Crossette': 0}


while firework_effects and explosive_power:

    if firework_effects[0] <= 0:
        del firework_effects[0]
        continue
    if explosive_power[-1] <= 0:
        del explosive_power[-1]
        continue

    first_firework_effect = firework_effects.popleft()
    last_explosive_power = explosive_power.pop()
    firework_sum = first_firework_effect + last_explosive_power

    if firework_sum % 3 == 0:
        if firework_sum % 5 != 0:
            fireworks['Palm'] += 1
        else:
            fireworks['Crossette'] += 1

    elif firework_sum % 5 == 0:
        if firework_sum % 3 != 0:
            fireworks['Willow'] += 1
        else:
            fireworks['Crossette'] += 1

    else:
        first_firework_effect -= 1
        firework_effects.append(first_firework_effect)
        explosive_power.append(last_explosive_power)

    if fireworks['Palm'] >= 3 and fireworks['Willow'] >= 3 and fireworks['Crossette'] >= 3:
        break

if fireworks['Palm'] >= 3 and fireworks['Willow'] >= 3 and fireworks['Crossette'] >= 3:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

print(f"Palm Fireworks: {fireworks['Palm']}")
print(f"Willow Fireworks: {fireworks['Willow']}")
print(f"Crossette Fireworks: {fireworks['Crossette']}")
