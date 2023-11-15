current_command = input()
total_coffee_needed = 0
while current_command != "END":
    if str.isupper(current_command):
        if current_command == "CODING":
            total_coffee_needed += 2
        elif current_command == "DOG" or current_command == "CAT":
            total_coffee_needed += 2
        elif current_command == "MOVIE":
            total_coffee_needed += 2
    elif str.islower(current_command):
        if current_command == "coding":
            total_coffee_needed += 1
        elif current_command == "dog" or current_command == "cat":
            total_coffee_needed += 1
        elif current_command == "movie":
            total_coffee_needed += 1
    current_command = input()
if total_coffee_needed > 5:
    print("You need extra sleep")
else:
    print(total_coffee_needed)
