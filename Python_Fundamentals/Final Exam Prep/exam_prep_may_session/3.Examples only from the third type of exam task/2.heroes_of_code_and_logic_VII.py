def creating_heroes(heroes):
    heroes_dictionary = {}

    for _ in range(heroes):
        hero_name, hp, mp = input().split()
        heroes_dictionary[hero_name] = [hp, mp]
    return heroes_dictionary


def modifying_dictionary_data(heroes_dictionary):
    MAX_HP = 100
    MAX_MANA = 200

    while True:
        command, *params = input().split(" - ")

        if command == "End":
            pass

        elif command == "CastSpell":
            hero_name, mp_needed, spell_name = params

            if heroes_dictionary[hero_name][1] >= mp_needed:
                heroes_dictionary[hero_name][1] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dictionary[hero_name][1]} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif command == "TakeDamage":
            hero_name, damage, attacker = params
            heroes_dictionary[hero_name][0] -= damage
            if heroes_dictionary[hero_name][0] > 0:
                current_hp = heroes_dictionary[hero_name][0]
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_dictionary[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif command == "Recharge":
            hero_name, amount = params
            amount_recovered = amount
            mp_before_recovery = heroes_dictionary[hero_name][1]
            heroes_dictionary[hero_name][1] += amount
            if int(heroes_dictionary[hero_name][1]) > MAX_MANA:
                heroes_dictionary[hero_name][1] = MAX_MANA
                amount_recovered = MAX_MANA - int(mp_before_recovery)
            print(f"{hero_name} recharged for {amount_recovered} MP!")

        elif command == "Heal":
            hero_name, amount = params
            amount_recovered = amount
            hp_before_recovery = heroes_dictionary[hero_name][0]
            heroes_dictionary[hero_name][0] += amount
            if int(heroes_dictionary[hero_name][0]) > MAX_HP:
                heroes_dictionary[hero_name][0] = MAX_HP
                amount_recovered = MAX_HP - int(hp_before_recovery)
            print(f"{hero_name} healed for {amount_recovered} HP!")


def base_function(heroes):
    heroes_dictionary = creating_heroes(heroes)
    modifying_dictionary = modifying_dictionary_data(heroes_dictionary)

    for hero_name, data in modifying_dictionary.items():
        hp, mp = data[0], data[1]
        print(f"{hero_name})"
               f"HP: {hp}"
               f"MP: {mp}")


n = int(input())
base_function(n)
