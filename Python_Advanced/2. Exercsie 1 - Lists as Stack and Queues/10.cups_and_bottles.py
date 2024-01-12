from collections import deque

cups_sequence = deque([int(x) for x in input().split()])
bottles_sequence = [int(x) for x in input().split()]
wasted_water = 0
while bottles_sequence and cups_sequence:
    bottle_liters = bottles_sequence.pop()
    glass_capacity = cups_sequence.popleft()

    if bottle_liters <= glass_capacity:
        glass_capacity -= bottle_liters
        if glass_capacity != 0:
            cups_sequence.appendleft(glass_capacity)
    else:
        wasted_water += bottle_liters - glass_capacity

if not bottles_sequence:
    print(f"Cups:", *cups_sequence)
else:
    print(f"Bottles:", *bottles_sequence)

print(f"Wasted litters of water: {wasted_water}")

