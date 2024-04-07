def password_decrypt(password):

    while True:
        command = input()

        if command.startswith("Done"):
            print(f"Your password is: {password}")
            break

        elif command.startswith("TakeOdd"):
            new_password = ""

            for index in range(len(password)):
                if index % 2 != 0:
                    new_password += password[index]
            password = new_password
            print(password)

        elif command.startswith("Cut"):
            current_command, index, length = command.split()
            password = password[:int(index)] + password[int(index) + int(length):]
            print(password)


        elif command.startswith("Substitute"):
            current_command, substring, substitute = command.split()
            if substring in password:
                password = password.replace(substring ,substitute)
                print(password)
            else:
                print("Nothing to replace!")



data = input()
password_decrypt(data)
