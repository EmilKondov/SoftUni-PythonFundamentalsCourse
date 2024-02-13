size = int(input())

matrix = []
ship_position = []

amount_of_fish = 0
no_whirpool = True

for row in range(size):
    matrix.append(list(input()))

    if "S" in matrix[row]:
        ship_position = [row, matrix[row].index("S")]
        matrix[row][matrix[row].index("S")] = "-"


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while command != "collect the nets":
    ship_next_row = ship_position[0] + directions[command][0]
    ship_next_col = ship_position[1] + directions[command][1]

    if not (0 <= ship_next_row < size and 0 <= ship_next_col < size):
        if ship_next_row < 0:
            ship_next_row = size - 1
        elif ship_next_row >= size:
            ship_next_row = 0

        if ship_next_col < 0:
            ship_next_col = size - 1
        elif ship_next_col >= size:
            ship_next_col = 0

    r, c = ship_next_row, ship_next_col
    ship_position = [r, c]
    symbol = matrix[r][c]


    if symbol == "W":
        no_whirpool = False
        amount_of_fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{','.join([str(x) for x in ship_position])}]")
        matrix[r][c] = "S"
        break
    if symbol.isdigit():
        amount_of_fish += int(symbol)

    matrix[r][c] = "-"
    command = input()

matrix[r][c] = "S"
if amount_of_fish < 20 and no_whirpool:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - amount_of_fish} tons of fish more.")
elif amount_of_fish >= 20:
    print("Success! You managed to reach the quota!")
if amount_of_fish > 0:
    print(f"Amount of fish caught: {amount_of_fish} tons.")
if no_whirpool:
    [print(*row, sep='') for row in matrix]


# 4
# ---S
# ----
# 9-5-
# 34--
# down
# down
# right
# down
# collect the nets


# 5
# S---9
# 777-1
# W333-
# 11111
# -----
# down
# down
# right
# down
# collect the nets

# 5
# S---9
# 777-1
# --5--
# 11W11
# 988--
# down
# down
# down
# down
# down
# down
# right
# right
# right
# collect the nets