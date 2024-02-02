import os

while True:
    command, *data = input().split("-")

    if command == "End":
        break
    elif command == "Create":
        with open(f"files/{data[0]}", "w"):
            pass
    elif command == "Add":
        with open(f"files/{data[0]}", "a") as file:
            file.write(f"{data[1]}\n")
    elif command == "Replace":
        try:
            with open(f"files/{data[0]}", "r+") as file:
                text = file.read()
                text = text.replace(data[1], data[2])

                file.seek(0)
                file.write(text)
                file.truncate()
        except FileNotFoundError:
            print(f"An error occurred!")
    elif command == "Delete":
        try:
            os.remove(f"files/{data[0]}")
        except FileNotFoundError:
            print(f"An error occurred!")


