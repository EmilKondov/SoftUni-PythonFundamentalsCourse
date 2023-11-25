sorted_list_to_do_notes = [0] * 10
while True:
    command = input()
    if command == 'End':
        break
    to_do_notes = command.split("-")
    priority = int(to_do_notes[0])
    note = to_do_notes[1]
    sorted_list_to_do_notes.pop(priority)
    sorted_list_to_do_notes.insert(priority, note)
result = [element for element in sorted_list_to_do_notes if element != 0]
print(result)

