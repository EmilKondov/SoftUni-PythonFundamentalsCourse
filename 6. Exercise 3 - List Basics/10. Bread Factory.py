initial_energy = 100
initial_coins = 100
factory_is_open = True


events = input().split("|")

for event in events:
    event_list = event.split("-")
    type_of_event = event_list[0]
    event_value = int(event_list[1])
    if type_of_event == 'rest':
        current_energy = initial_energy
        initial_energy += event_value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = abs(current_energy - initial_energy)
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif type_of_event == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            initial_energy += 50
            print(f"You had to rest!")
    else:
        if initial_coins >= event_value:
            initial_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            factory_is_open = False
            break
if factory_is_open:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
