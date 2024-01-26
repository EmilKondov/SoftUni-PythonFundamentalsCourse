first_line = input()
while True:
    entry_data = input()

    if entry_data.isdigit():
        entry_data = int(entry_data)
        print(first_line * entry_data)
        break
    else:
        print("Variable times must be an integer")

