def add(list_lessons, title):
    if title not in list_lessons:
        list_lessons.append(title)
    return list_lessons

def insert(list_lessons, title, index):
    if title not in list_lessons:
        list_lessons.insert(index, title)
    return  list_lessons

def remove(lessons, title):
    pass

def swap(lessons, title):
    pass

def exercise(lessons, title):
    pass



lessons = input().split(", ")
command = input()
while command != "course start":
    command = command.split(":")
    action, title = command[0], command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]
    elif action == "Add":
        lessons = add(lessons, title)
    elif action == "Insert":
        lessons = insert(lessons, title, index_or_lesson_title)
    elif action == "Remove":
        remove(lessons, title)
    elif action == "Swap":
        swap(lessons, title)
    elif action =="Exercise":
        exercise(lessons, title)
    command = input()

