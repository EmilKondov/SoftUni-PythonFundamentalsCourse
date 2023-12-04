######### Условие №№№№

# Help plan the next Programming Fundamentals course by keeping track of the lessons that will be included in the
# course and all the exercises for the lessons. Before the course starts, there are some changes to be made.
# On the first input line, you will receive the initial schedule of lessons and exercises that will be part of the next
# course, separated by a comma and a space ", ". Until you receive the "course start" command, you will be
# given some commands to modify the course schedule.
# The possible commands are:
# • "Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
# • "Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
# • "Remove:{lessonTitle}" - remove the lesson, if it exists.
# • "Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
# • "Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, if the lesson
# exists and there is no exercise already, in the following format "{lessonTitle}-Exercise". If the
# lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
#Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are
#any following the lessons.
#Input / Constraints
#• On the first line - the initial schedule lessons - strings, separated by comma and space ", ".
#• Until "course start" you will receive commands in the format described above.
#Output
#• Print the whole course schedule, each lesson on a new line with its number (index) in the schedule:
#"{lesson index}.{lessonTitle}".
#• Allowed working time / memory: 100ms / 16MB.




def add(lessons, title):
    if title not in lessons:
        lessons.append(title)
    return lessons

def insert(lessons, title, index):
    if title not in lessons:
        lessons.insert(index, title)
    return  lessons

def remove(lessons, title):
    if title in lessons:
        title_index = lessons.index(title)
        if title_index + 1 in range(len(lessons)):
            if "Exercise" in lessons[title_index + 1]:
                lessons.pop(title_index + 1)
        lessons.remove(title)
    return lessons

def swap(lessons, first_lesson, second_lesson):
    if first_lesson in lessons and second_lesson in lessons:
        first_lesson_index = lessons.index(first_lesson)
        second_lesson_index = lessons.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_lesson_index + 1 in range(len(lessons)):
            first_has_exercise = "Exercise" in lessons[first_lesson_index + 1]  # boolean директно изразяваме, че first_has_exercise = True
        if second_lesson_index + 1 in range(len(lessons)):
            second_has_exercise = "Exercise" in lessons[second_lesson_index + 1]
        lessons[first_lesson_index], lessons[second_lesson_index] = lessons[second_lesson_index], lessons[first_lesson_index]
        if first_has_exercise and second_has_exercise:
            lessons[first_lesson_index + 1], lessons[second_lesson_index +1] = lessons[second_lesson_index + 1], lessons[first_lesson_index + 1]
        elif not first_has_exercise and second_has_exercise:
            lessons.insert(first_lesson_index + 1, lessons.pop(second_lesson_index + 1))
        elif first_has_exercise and not second_has_exercise:
            lessons.insert(second_lesson_index + 1, lessons.pop(first_lesson_index + 1))
    return lessons

def exercise(lessons, title):
    if title in lessons and f"{title}-Exercise" not in lessons:
        title_index = lessons.index(title)
        lessons.insert(title_index + 1, f"{title}-Exercise")
    elif title not in lessons and f"{title}-Exercise" not in lessons:
        lessons.append(title)
        lessons.append(f"{title}-Exercise")
    return lessons


lessons = input().split(", ")
command = input()

while command != "course start":
    command = command.split(':')
    action, title = command[0], command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]
    if action == "Add":
        lessons = add(lessons, title)
    elif action == "Insert":
        lessons = insert(lessons, title, int(index_or_lesson_title))
    elif action == "Remove":
        lessons = remove(lessons, title)
    elif action == "Swap":
        lessons = swap(lessons, title, index_or_lesson_title)
    elif action =="Exercise":
        lessons = exercise(lessons, title)
    command = input()
for index, lessons_name in enumerate(lessons):
    print(f"{index + 1}.{lessons_name}")
