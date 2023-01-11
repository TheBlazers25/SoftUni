class Class:

    students = []
    grades = []
    __students_count = 22

    def __init__(self, name):
        self.name = name

    def add_student(self, students: str, grade: float):
        if Class.__students_count > 0:
            Class.students.append(students)
            Class.grades.append(grade)
            Class.__students_count -= 1

    def get_average_grade(self):
        average_grade = f"{(sum(Class.grades) / len(Class.grades)):.2f}"
        return float(average_grade)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {Class.get_average_grade(self)}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)