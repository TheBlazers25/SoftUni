lines = int(input())

max_capacity = 255
total_liters = 0

for line in range(lines):
    liters = int(input())
    if max_capacity - liters >= 0:
        max_capacity += - liters
        total_liters += liters
    else:
        print("Insufficient capacity!")
print(total_liters)
