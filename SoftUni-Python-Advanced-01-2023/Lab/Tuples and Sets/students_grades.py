number_of_students = int(input())
students_dictionary = {}

for i in range(number_of_students):
    name, grade = input().split(' ')
    if name not in students_dictionary:
        students_dictionary[name] = []

    students_dictionary[name].append(float(grade))

for key, value in students_dictionary.items():
    convert_grade_to_string = " ".join(map(lambda grade: f'{grade:.2f}', value))
    avg_grade = sum(value) / len(value)
    print(f'{key} -> {convert_grade_to_string} (avg: {avg_grade:.2f})')
