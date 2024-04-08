fighters_dictionary = {}
while True:
    command = input()

    if command == "Results":
        result = (f"People count: {len(fighters_dictionary)}")
        print(result)
        for name, data in fighters_dictionary.items():
            health, energy = data[0],data[1]
            print(f"{name} - {health} - {energy}")

    elif command.startswith("Add"):
        current_command, person_name, health, energy = command.split(":")
        if person_name in fighters_dictionary:
            fighters_dictionary[person_name][0] = int(fighters_dictionary[person_name][0]) + int(health)
        else:
            fighters_dictionary[person_name] = [health, energy]

    elif command.startswith("Attack"):
        current_command, attacker_name, defender_name, damage = command.split(":")
        if fighters_dictionary[defender_name]:
            fighters_dictionary[defender_name][0] = int(fighters_dictionary[defender_name][0]) - int(damage)

            if int(fighters_dictionary[defender_name][0]) <= 0:
                del fighters_dictionary[defender_name]
                print(f"{defender_name} was disqualified!")

        if fighters_dictionary[attacker_name]:
            fighters_dictionary[attacker_name][1] = int(fighters_dictionary[attacker_name][1]) - 1

            if int(fighters_dictionary[attacker_name][1]) <= 0:
                del fighters_dictionary[attacker_name]
                print(f"{attacker_name} was disqualified!")


    elif command.startswith("Delete"):
        current_command, username = command.split(":")
        if username == "All":
            fighters_dictionary.clear()

        elif fighters_dictionary[username]:
            del fighters_dictionary[username]






