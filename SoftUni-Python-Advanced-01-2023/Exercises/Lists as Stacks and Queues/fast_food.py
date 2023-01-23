from collections import deque

food_quantity = int(input())
food_quantity_queue = deque([int(n) for n in input().split()])

# food_counter = 0

print(max(food_quantity_queue))

for food in food_quantity_queue.copy():

    if food_quantity - food >= 0:
        food_quantity_queue.popleft()
        food_quantity -= food

    else:
        print(f'Orders left: {" ".join([str(f) for f in food_quantity_queue])}')
        break

else:
    print('Orders complete')