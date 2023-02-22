from collections import deque

egg_size = deque(int(n) for n in input().split(', '))
paper_size = [int(n) for n in input().split(', ')]

filled_boxes = 0

while True:

    if not egg_size:
        break

    if not paper_size:
        break

    current_egg_size = egg_size.popleft()
    current_paper_size = paper_size.pop()

    if current_egg_size == 13:
        paper_size.append(current_paper_size)
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]

    elif current_egg_size > 0:
        sum_of_egg_and_paper_size = current_egg_size + current_paper_size
        if sum_of_egg_and_paper_size <= 50:
            filled_boxes += 1

    else:
        paper_size.append(current_paper_size)

if filled_boxes > 0:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if paper_size:
    print('Pieces of paper left:', ', '.join(map(str, paper_size)))
if egg_size:
    print('Eggs left:', ', '.join(map(str, egg_size)))
