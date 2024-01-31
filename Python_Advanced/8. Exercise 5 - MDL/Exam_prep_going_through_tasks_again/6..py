size = 5
matrix = []

shooter_position = []
total_targets = 0
shot_targets = 0
shot_targets_coordinates = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        shooter_position = [row, matrix[row].index("A")]

    if "x" in matrix[row]:
        total_targets += matrix[row].count("x")

count_of_commands = int(input())
for command in range(count_of_commands):
    command = input().split()

    action, direction, *steps = command

    if action == "move":

        r = shooter_position[0] + directions[direction][0] * int(*steps)
        c = shooter_position[1] + directions[direction][1] * int(*steps)


        if (0 <= r < size and 0 <= c < size) and matrix[r][c] == ".":
            shooter_position = [r, c]



    elif action == "shoot":
        shot_row = shooter_position[0] + directions[direction][0]
        shot_col = shooter_position[1] + directions[direction][1]

        while 0 <= shot_row < size and 0 <= shot_col < size:

            if matrix[shot_row][shot_col] == "x":
                total_targets -= 1
                shot_targets += 1
                shot_targets_coordinates.append([shot_row, shot_col])

            shot_row += directions[direction][0]
            shot_col += directions[direction][1]
if shot_targets <= total_targets:
    print(f"Training not completed! {total_targets} targets left.")
else:
    print(f"Training completed! All {shot_targets} targets hit.")
print(*shot_targets_coordinates, sep="\n")
