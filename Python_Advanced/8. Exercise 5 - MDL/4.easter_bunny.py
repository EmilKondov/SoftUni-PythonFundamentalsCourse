field_size = int(input())
field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

path = []
total_eggs = 0
best_direction = []


for row in range(field_size):
    for col in range(field_size):
        if field[row][col] == "B":
            bunny_row, bunny_col = row, col

            for direction in directions:
                while True:
                    if direction == "up":
                        next_row, next_col = directions[direction][0] + bunny_row, directions[direction][1] + bunny_col

                    if direction == "down":
                        pass
                    if direction == "left":
                        pass
                    if direction == "right":
                        pass







# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0