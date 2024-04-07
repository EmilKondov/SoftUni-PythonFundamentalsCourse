def decrypt_message(message):

    while True:
        command = input()


        if command.startswith("Decode"):
            print(f"The decrypted message is: {message}")
            break

        elif command.startswith("Move"):
            current_command, number_of_letters = command.split("|")
            letters_to_be_moved = message[:int(number_of_letters)]
            message = message[int(number_of_letters):] + letters_to_be_moved


        elif command.startswith("Insert"):
            current_command, index, value = command.split("|")
            message = message[:int(index)] + value + message[int(index):]


        elif command.startswith("ChangeAll"):
            current_command, substring, replacement = command.split("|")
            message = message.replace(substring, replacement)


data = input()
decrypt_message(data)
