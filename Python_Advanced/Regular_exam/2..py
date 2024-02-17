size = int(input())
ARMOUR = 300

matrix = []
jet_pos = []

enemies = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(list(input()))

    if "J" in matrix[row]:
        jet_pos = [row, matrix[row].index("J")]
        matrix[row][matrix[row].index("J")] = "-"

    if "E" in matrix[row]:
        enemies += matrix[row].count("E")


while ARMOUR and enemies:
    command = input()

    next_jet_row = jet_pos[0] + directions[command][0]
    next_jet_col = jet_pos[1] + directions[command][1]

    # if not(0 <= next_jet_row < size and 0 <= next_jet_col < size):
    #     pass

    r, c = next_jet_row, next_jet_col
    jet_pos = [r, c]

    if matrix[r][c] == "R":
        ARMOUR = 300
        matrix[r][c] = "-"
    elif matrix[r][c] == "E":
        enemies -= 1
        matrix[r][c] = "-"
        if not enemies:
            print("Mission accomplished, you neutralized the aerial threat!")
            matrix[r][c] = "J"
            break
        else:
            ARMOUR -= 100
            if ARMOUR == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")
                matrix[r][c] = "J"
[print(*row,sep='') for row in matrix]

