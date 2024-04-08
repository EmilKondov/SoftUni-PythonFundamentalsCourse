string = ""
while True:
    command = input()

    if command.startswith("End"):
        break

    elif command.startswith("Add"):
        current_command, substring = command.split()
        string = string + substring


    elif command.startswith("Upgrade"):
        current_command, char = command.split()
        next_char = ord(char) + 1
        string = string.replace(char,chr(next_char))

    elif command.startswith("Print"):
        print(string)


    elif command.startswith("Index"):
        current_command, char = command.split()
        if char not in string:
            print("None")
        for index in range(len(string)):
            if string[index] == char:
                print(index, end=" ")
        print("")

    elif command.startswith("Remove"):
        current_command, substring = command.split()
        string = string.replace(substring, "")
