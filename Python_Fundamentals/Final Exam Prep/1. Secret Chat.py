def secret_chat(message):

    while True:
        command = input()

        if command.startswith("Reveal"):
            print(f"You have a new text message: {message}")
            break

        elif command.startswith("InsertSpace"):
            current_comand, index = command.split(":|:")
            message = message[:int(index)] + " " + message[int(index):]
            print(message)

        elif command.startswith("Reverse"):
            current_command, substring = command.split(":|:")
            if substring in message:
                message = message.replace(substring, "", 1)
                message = message + substring[::-1]
                print(message)
            else:
                print("error")


        elif command.startswith("ChangeAll"):
            current_command, substring, replacement = command.split(":|:")
            message = message.replace(substring, replacement)
            print(message)

initial_message = input()
secret_chat(initial_message)
