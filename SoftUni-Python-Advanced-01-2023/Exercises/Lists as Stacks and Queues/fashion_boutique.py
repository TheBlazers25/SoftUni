clothes = [int(n) for n in input().split()]
capacity = int(input())

counter = 1
rack_space = capacity

while clothes:
    last_piece = clothes.pop()

    if rack_space - last_piece >= 0:
        rack_space -= last_piece

    else:
        counter += 1
        rack_space = capacity - last_piece

print(counter)