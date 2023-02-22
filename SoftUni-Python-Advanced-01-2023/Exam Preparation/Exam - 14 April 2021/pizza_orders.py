from collections import deque

pizza_orders = deque(int(n) for n in input().split(', '))
employees_capacity = [int(n) for n in input().split(', ')]

pizzas_made = 0

while pizza_orders and employees_capacity:
    pizzas = pizza_orders.popleft()

    if pizzas > 10 or pizzas <= 0:
         continue

    employee = employees_capacity.pop()
    if pizzas <= employee:
        pizzas_made += pizzas

    elif pizzas > employee:
        remaining_pizzas = pizzas - employee
        pizzas_made += employee
        pizza_orders.appendleft(remaining_pizzas)

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    print(f'Employees: {", ".join(map(str, employees_capacity))}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str, pizza_orders))}')



# while pizza_orders and employees_capacity:
#     pizzas = pizza_orders[0]
#     employee = employees_capacity[-1]
#
#     if pizzas > 10 or pizzas <= 0:
#         pizza_orders.popleft()
#
#     elif pizzas <= employee:
#         pizza_orders.popleft()
#         employees_capacity.pop()
#         pizzas_made += pizzas
#
#     elif pizzas > employee:
#         remaining_pizzas = pizzas - employee
#         pizzas_made += employee
#         employees_capacity.pop()
#         pizza_orders.popleft()
#         pizza_orders.appendleft(remaining_pizzas)
