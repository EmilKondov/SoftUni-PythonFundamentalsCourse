from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())

current_light_duration = green_light_duration
current_free_window_duration = free_window_duration
passed_cars_counter = 0

crash = False

while current_light_duration != 0:
    command = input()
    if command == "END":
        break
    if command == "green":
        current_light_duration = green_light_duration
        current_free_window_duration = free_window_duration
    else:
        current_car_passing_time = len(command)
        if current_car_passing_time <= current_light_duration:
            passed_cars_counter += 1
            current_light_duration -= current_car_passing_time
        else:
            characters_to_remove = current_light_duration
            if len(command[characters_to_remove:]) < current_free_window_duration:
                current_free_window_duration -= 1
                passed_cars_counter += 1
                current_light_duration = 0
            else:
                character_hit = len(command[:characters_to_remove]) - current_free_window_duration
                print("A crash happened!")
                print(f"{command} was hit at {command[character_hit]}.")
                crash= True
                break
if not crash:
    print(f"""Everyone is safe.
    {passed_cars_counter} total cars passed the crossroads.""")
