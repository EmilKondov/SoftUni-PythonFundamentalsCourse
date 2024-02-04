#Input
size = int(input())
commands = input().split(", ")

matrix = []
squirrel_position = []
hazelnuts = 0

for row in range(size):
    matrix.append(list(input()))
    if "s" in matrix[row]:
        squirrel_position = [row, matrix[row].index("s")]
        matrix[row][squirrel_position[1]] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for command in commands:
    if hazelnuts >= 3:
        break

    squirrel_next_row = squirrel_position[0] + directions[command][0]
    squirrel_next_col = squirrel_position[1] + directions[command][1]

    if not (0 <= squirrel_next_row < size and 0 <= squirrel_next_col < size):
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnuts}")
        exit()

    r, c = squirrel_next_row, squirrel_next_col
    squirrel_position = [r, c]

    if matrix[r][c] == "h":
        hazelnuts += 1
        matrix[r][c] = "*"

    elif matrix[r][c] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {hazelnuts}")
        exit()

if hazelnuts >= 3:
    print("Good job! You have collected all hazelnuts!")
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
