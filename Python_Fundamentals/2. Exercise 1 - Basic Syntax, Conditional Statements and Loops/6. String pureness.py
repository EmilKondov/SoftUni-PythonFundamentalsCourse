n = input()

for current_string in range(n):
    current_string = input()
    for character in current_string:
        if character == "," or  character == "." or character == "_":
            print(f"{current_string} is not pure!")
            break
    else:
        print(f"{current_string} is pure.")
