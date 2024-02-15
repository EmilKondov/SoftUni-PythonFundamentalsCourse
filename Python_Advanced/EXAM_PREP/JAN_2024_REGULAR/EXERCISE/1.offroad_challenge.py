from collections import deque

#Read the sequences under the correct type
fuel_collection = [int(x) for x in input().split()]
additional_consumption = deque([int(y) for y in input().split()])
needed_fuel = deque([int(z) for z in input().split()])

altitude_count = 0


while fuel_collection and additional_consumption and needed_fuel:
    current_fuel = fuel_collection[-1]
    current_consumption = additional_consumption[0]
    current_needed_fuel = needed_fuel[0]
    difference = current_fuel - current_consumption

    if difference >= current_needed_fuel:
        fuel_collection.pop()
        additional_consumption.popleft()
        needed_fuel.popleft()
        altitude_count += 1
        # altitudes.append(f"Altitude {index}")
        print(f"John has reached: Altitude {altitude_count}")
    else:
        print(f"John did not reach: Altitude {altitude_count + 1}")
        # failed = True
        break

if fuel_collection and altitude_count:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join([f'Altitude {num}' for num in range(1, altitude_count + 1)])}")
elif fuel_collection and not altitude_count:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

if not fuel_collection:
    print("John has reached all the altitudes and managed to reach the top!")
