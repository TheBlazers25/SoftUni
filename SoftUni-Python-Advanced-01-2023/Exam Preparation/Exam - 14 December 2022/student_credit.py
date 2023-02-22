def students_credits(*args):
    total_credits = 0
    diyan_course_info = {}
    final_string = []

    for info in args:
        course, credits, max_test_points, diyan_points = info.split('-')
        current_percentage = int(diyan_points) / int(max_test_points)
        current_credits = int(credits) * current_percentage
        total_credits += current_credits
        diyan_course_info[course] = current_credits

    if total_credits >= 240:
        final_string.append(f"Diyan gets a diploma with {total_credits} credits.")
    else:
        final_string.append(f"Diyan needs {240 - total_credits} credits more for a diploma.")

    sorted_course_info = sorted(diyan_course_info.items(), key=lambda x: -x[1])
    for course, points in sorted_course_info:
        final_string.append(f"{course} - {float(points):.1f}")

    return "\n".join(final_string)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)