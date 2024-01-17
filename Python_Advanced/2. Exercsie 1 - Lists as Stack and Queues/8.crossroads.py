### Initial solution -- finaly works ###
from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())

car_passed = 0
cars = deque()

crash = False

while True:
    data = input()

    if data == "END":
        break
    elif data != "green":
        cars.append(data)
    else:
        current_light_duration = green_light_duration
        current_free_window_duration = free_window_duration

        while current_light_duration > 0 and cars:
            car = cars.popleft()

            if len(car) <= current_light_duration:
                current_light_duration -= len(car)
                car_passed += 1
            else:
                left_char = current_light_duration - len(car)
                current_light_duration = 0
                if len(car[left_char:]) <= current_free_window_duration:
                    car_passed += 1
                    current_free_window_duration -= len(car[left_char:])
                else:
                    character_hit = len(car[:left_char]) - current_free_window_duration
                    print("A crash happened!")
                    print(f"{car} was hit at {car[character_hit]}.")
                    crash = True
                    exit()

if not crash:
    print(f"""Everyone is safe.                                                    
{car_passed} total cars passed the crossroads.""")


### Second try -- second solution ###

#
# from collections import deque
# green_light_duration = int(input())
# free_window_duration = int(input())
#
#
# car_passed = 0
# cars = deque()
#
# crash = False
#
# while True:
#     data = input()
#
#     if data == "END":
#         break
#     if data != "green":
#         cars.append(data)
#     else:
#         current_light_duration = green_light_duration
#         current_free_window_duration = free_window_duration
#
#         while current_light_duration > 0 and cars:
#             car = cars.popleft()
#
#
#             if len(car) <= current_light_duration:
#                 current_light_duration -= len(car)
#                 car_passed += 1
#             else:
#                 left_char = current_light_duration - len(car)
#                 if len(car[left_char:]) <= current_free_window_duration:
#                     car_passed += 1
#                     current_free_window_duration -= len(car[left_char:])
#                     current_light_duration = 0
#                 else:
#                     print("A crash happened!")
#                     print(f"{car} was hit at {car[current_light_duration + free_window_duration]}.")
#                     crash = True
#                     break
#     if crash:
#         break
#
# if not crash:
#     print(f"""
# Everyone is safe.
# {car_passed} total cars passed the crossroads.""")
#


#### Third almost the same solution ###

### my latest working code ###

# from collections import deque
#
# green_light_duration = int(input())
# free_window_duration = int(input())
#
# car_passed = 0
# cars = deque()
# crash = False
#
# while True:
#     data = input()
#
#     if data == "END":
#         break
#
#     if data != "green":
#         cars.append(data)
#     else:
#         current_light_duration = green_light_duration
#
#         while current_light_duration > 0 and cars:
#             car = cars.popleft()
#
#             if len(car) <= current_light_duration:
#                 current_light_duration -= len(car)
#                 car_passed += 1
#             elif len(car) <= current_light_duration + free_window_duration:
#                 car_passed += 1
#                 break
#             else:
#                 print("A crash happened!\n"
#                       f"{car} was hit at {car[current_light_duration + free_window_duration]}.")
#                 crash = True
#                 break
#     if crash:
#         break
#
# if not crash:
#     print(f"""
# Everyone is safe.
# {car_passed} total cars passed the crossroads.""")
