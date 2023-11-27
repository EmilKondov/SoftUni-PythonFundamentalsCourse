current_string = input()
while current_string != "End":
    if current_string == "SoftUni":
        continue
    new_string = ""
    for character in current_string:
        new_string += character * 2
    print(new_string)
    current_string = input()

