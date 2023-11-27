############### First Way #####################

#sorted_list_to_do_notes = [0] * 10
#while True:
#    command = input()
#    if command == 'End':
#        break
#    to_do_notes = command.split("-")
#    priority = int(to_do_notes[0])
#    note = to_do_notes[1]
#    sorted_list_to_do_notes.pop(priority)
#    sorted_list_to_do_notes.insert(priority, note)
#result = [element for element in sorted_list_to_do_notes if element != 0]
#print(result)
#
########## Second Way #############################

def to_do_notes():
    todo_notes = []

    while True:
        note = input()
        if note == 'End':
            break

        todo_notes.append(note)
    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
    result_sorted_notes = [todo_notes.split("-")[1] for todo_notes in sorted_notes]
    return result_sorted_notes

result = to_do_notes()
print(result)
