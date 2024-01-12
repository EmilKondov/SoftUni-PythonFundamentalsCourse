number_of_students = int(input())

students_data = {}

for student in range(number_of_students):
    name, grade_str = input().split()
    grade = float(grade_str)

    if name not in students_data:
        students_data[name] = []
    students_data[name].append(grade)

for student, grade in students_data.items():
    formatted_grade = f"{' '.join([f'{g:.2f}' for g in grade])}"
    print(f"{student} ->",f"{formatted_grade}", (f"(avg: {(sum(grade) / len(grade)):.2f})"))
