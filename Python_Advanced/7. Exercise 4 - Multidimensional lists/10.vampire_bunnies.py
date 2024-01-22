def player_position():
    for row in range(rows):
        if "P" in matrix[row]:
            return row, matrix[row].index("P")

def check_valid_position():
    if 0 <= player_movement_row < rows and 0 <= player_movement_column < columns:
        pass
    else:

rows, columns = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = input() 
win = False

player_row, player_column = player_position()
matrix[player_row][player_column] = "."

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0,-1),
    "R": (0, 1)
}

for command in commands:
    if command in directions:
        player_movement_row, player_movement_column = player_row + directions[command][0], player_column + directions[command][1]
        if check_valid_position():




print(matrix)

# 5 6
# .....P
# ......
# ...B..
# ......
# ......
# ULDDDR