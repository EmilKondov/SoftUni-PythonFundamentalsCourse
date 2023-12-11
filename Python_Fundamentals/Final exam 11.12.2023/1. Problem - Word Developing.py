final_string = ""
flag = False
while True:
    command = input()
    
    if command.startswith("End"):
        break

    elif command.startswith("Add"):
        current_command, substring = command.split()
        final_string = final_string + substring

    elif command.startswith("Upgrade"):
        current_command, char = command.split()
        ascii_number_current_char = ord(char)
        replacement = chr(ascii_number_current_char + 1)
        if char in final_string:
            final_string = final_string.replace(char, replacement)
      
            
    elif command.startswith("Print"):
        print(final_string)

    elif command.startswith("Index"):
        current_command, char = command.split()
        for character in range(len(final_string)):
            index_occur = character
            symbol = final_string[character]
            if symbol == char:
                print(index_occur, end=" ")
                flag = True
        if flag is False:
            print(None)
        print()


    elif command.startswith("Remove"):
        current_command, substring = command.split()
        if substring in final_string:
            final_string = final_string.replace(substring, "")

