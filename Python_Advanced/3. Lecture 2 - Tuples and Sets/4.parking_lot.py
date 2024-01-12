given_car_numbers = int(input())

cars = set()

for car in range(given_car_numbers):
    action, car_number = input().split(", ")

    if action == "IN":
        cars.add(car_number)
    elif action == "OUT":
        if car_number in cars:
            cars.remove(car_number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")