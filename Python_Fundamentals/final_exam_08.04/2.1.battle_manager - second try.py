data = input()

fighters_dictionary = {}

while data != "Results":
    splitted_data = data.split(":")
    current_command, *params = splitted_data

    if current_command == "Add":
        name = params[0]
        health = int(params[1])
        energy = int(params[2])

        if name not in fighters_dictionary:
            fighters_dictionary[name] = {"health": health, "energy": energy}
        else:
            fighters_dictionary[name]["health"] += health

    elif current_command == "Attack":
        attacker_name = params[0]
        defender_name = params[1]
        damage = int(params[2])

        if attacker_name and defender_name in fighters_dictionary:
            fighters_dictionary[defender_name]["health"] -= damage
            fighters_dictionary[attacker_name]["energy"] -= 1

            if fighters_dictionary[defender_name]["health"] <= 0:
                print(f"{defender_name} was disqualified!")
                del fighters_dictionary[defender_name]

            if fighters_dictionary[attacker_name]["energy"] <= 0:
                print(f"{attacker_name} was disqualified!")
                del fighters_dictionary[attacker_name]

    elif current_command == "Delete":
        username = params[0]

        if username == "All":
            fighters_dictionary.clear()

        elif username in fighters_dictionary:
            del fighters_dictionary[username]

    data = input()

result = (f"People count: {len(fighters_dictionary)}")
print(result)
for name, data in fighters_dictionary.items():
    health1 = data["health"]
    energy1 = data["energy"]
    print(f"{name} - {health1} - {energy1}")
