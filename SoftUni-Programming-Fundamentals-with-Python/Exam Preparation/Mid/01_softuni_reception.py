first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())
time_needed = 0

all_employees = first_employee + second_employee + third_employee

while students_count > 0:
    time_needed += 1
    if time_needed % 4 != 0:
        students_count -= all_employees
    elif students_count <= 0:
        break

print(f'Time needed: {time_needed}h.')