SIZE = 6

matrix = []
rover_pos = []
deposit_pos = []

deposits = {"Water": 0, "Metal": 0, "Concrete": 0}
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


for row in range(SIZE):
    matrix.append(input().split())

    if "E" in matrix[row]:
        rover_pos = [row, matrix[row].index("E")]
        matrix[row][matrix[row].index("E")] = "-"

commands = input().split(", ")
for command in commands:
    current_command = command

    rover_new_row = rover_pos[0] + directions[current_command][0]
    rover_new_col = rover_pos[1] + directions[current_command][1]

    if not (0 <= rover_new_row < SIZE or 0 <= rover_new_col < SIZE):
        print("a")

    r, c = rover_new_row, rover_new_col
    rover_pos = [r, c]

    if matrix[r][c] == "R":
        print(f"Rover got broken at({r}, {c})")
        break
    if matrix[r][c] == "W" or matrix[r][c] == "M" or matrix[r][c] == "C"
        deposits[matrix[r][c]] += 1
        print(f"")
