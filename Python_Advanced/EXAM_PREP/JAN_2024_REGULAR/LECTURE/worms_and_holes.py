from collections import deque

worm_size = [int(x) for x in input().split()]
hole_size = deque(int(y) for y in input().split())

matches_count = 0
count_of_worms = len(worm_size)

while worm_size and hole_size:
    current_worm = worm_size[-1]
    current_hole = hole_size[0]

    if current_worm == current_hole:
        matches_count += 1
        worm_size.pop()
        hole_size.popleft()
    else:
        hole_size.popleft()
        worm_size[-1] -= 3
        if worm_size[-1] <= 0:
            worm_size.pop()

if matches_count:
    print(f"Matches: {matches_count}")
else:
    print(f"There are no matches.")


if not worm_size and matches_count == count_of_worms:
    print("Every worm found a suitable hole!")
if not worm_size and matches_count != count_of_worms:
    print("Worms left: none")
if worm_size:
    print(f"Worms left: {', '.join(str(x) for x in worm_size)}")

if not hole_size:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(y) for y in hole_size)}")
