# Input

size = int(input())
field = []
bunny_position = []

best_direction = None
path = []
max_eggs_collected = float("-inf")

directions = {

    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    field.append(input().split())

    if "B" in field[row]:
        bunny_position =[row, field[row].index("B")]



# LOGIC

for direction, coordinates in directions.items():
    row, col = [
        bunny_position[0] + directions[direction][0],
        bunny_position[1] + directions[direction][1]
    ]

    current_path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:

        if field[row][col] == "X":
            break

        collected_eggs += int(field[row][col])
        current_path.append([row, col])

        row += directions[direction][0]
        col += directions[direction][1]

    if collected_eggs >= max_eggs_collected:
        max_eggs_collected = collected_eggs
        path = current_path
        best_direction = direction

print(best_direction)
[print(row) for row in path]
print(max_eggs_collected)
