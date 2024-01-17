from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
stuck_cars = []

current_light_duration = green_light_duration
current_free_window_duration = free_window_duration
passed_cars_counter = 0

while True:
    command = input()
    if command == "END":
        break
    if command == "green":
        current_light_duration = green_light_duration

    else:
        current_car_passing_time = len(command)
        if current_car_passing_time <= current_light_duration:
            passed_cars_counter += 1
            cars.append(command)
            current_light_duration -= current_car_passing_time
        else:
            characters_to_remove = current_light_duration
            stuck_cars.append(command[:characters_to_remove])
            if len(command) <= current_free_window_duration:
                current_free_window_duration -= 1
                stuck_cars.append(command)
                cars.add(stuck_cars[0])
                passed_cars_counter += 1