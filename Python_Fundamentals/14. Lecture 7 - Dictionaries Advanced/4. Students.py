students = []
corresponding_course = ""

while True:
    student_info = input()


    if ":" not in student_info:
        corresponding_course = student_info
        break

    name, ID, course = student_info.split(":")
    students.append({'name': name, 'ID': ID, 'course': course})

for student in students:
    if corresponding_course.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")
