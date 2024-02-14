from collections import deque
n = 4

fuel_collection = [int(x) for x in input().split()]
additional_consumption = deque([int(y) for y in input().split()])
needed_fuel = deque([int(z) for z in input().split()])

altitudes = []
failed = False

for index in range(1, n + 1):

    current_fuel = fuel_collection[-1]
    current_consumption = additional_consumption[0]
    current_needed_fuel = needed_fuel[0]

    if abs(current_fuel - current_consumption) >= current_needed_fuel:
        fuel_collection.pop()
        additional_consumption.popleft()
        needed_fuel.popleft()
        altitudes.append(f"Altitude {index}")
        print(f"John has reached: Altitude {index}")

    elif abs(current_fuel - current_consumption) < current_needed_fuel and not altitudes:
        print("John failed to reach the top.John didn't reach any altitude.")
        exit()
    else:
        print(f"John did not reach: Altitude {index}")
        print(f"John failed to reach the top.")
        failed = True
        break

if failed:
    print(f"Reached altitudes: {', '.join(altitudes)}")
else:
    print(f"John has reached all the altitudes and managed to reach the top!")
