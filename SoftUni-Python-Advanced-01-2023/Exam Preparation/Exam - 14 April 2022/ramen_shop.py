from collections import deque

bowls_of_ramen = [int(n) for n in input().split(', ')]
customers = deque(int(n) for n in input().split(', '))

while True:

    if not customers:
        break

    if not bowls_of_ramen:
        break

    last_bowl = bowls_of_ramen.pop()
    first_customer = customers.popleft()

    if last_bowl > first_customer:
        bowl_value = last_bowl - first_customer
        bowls_of_ramen.append(bowl_value)

    elif first_customer > last_bowl:
        customer_value = first_customer - last_bowl
        customers.appendleft(customer_value)

if not customers:
    print('Great job! You served all the customers.')
    if bowls_of_ramen:
        print(f'Bowls of ramen left: {", ".join(map(str, bowls_of_ramen))}')

elif not bowls_of_ramen:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f'Customers left: {", ".join(map(str, customers))}')
