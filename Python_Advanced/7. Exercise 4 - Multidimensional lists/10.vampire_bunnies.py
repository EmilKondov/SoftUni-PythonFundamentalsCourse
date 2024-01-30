def player_position():
    for row in range(rows):
        if "P" in matrix[row]:
            return row, matrix[row].index("P")

def check_valid_position(row, col, player=False ):
    global win

    if 0 <= row < rows and 0 <= col < columns:
        return True
    if player:
        win = True

def bunny_position():
    bunny_positions_list = []

    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] == "B":
                bunny_positions_list.append([row, col])

    return bunny_positions_list


def bunny_move(bunny_position):
    for row, col in bunny_position:
        for bunnie_move in directions.values():
            new_row, new_col = row + bunnie_move[0], col + bunnie_move[1]

            if check_valid_position(new_row, new_col):
                matrix[new_row][new_col] = "B"


def check_player_alive(row, column):
    if matrix[row][column] == "B":
        show_results("dead")

def show_results(status="won"):
    [print(*row, sep="") for row in matrix]
    print(f"{status}: {player_row} {player_column}")

    raise SystemExit


# прочитаме си даните
rows, columns = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]

commands = input()

win = False
directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0,-1),
    "R": (0, 1)
}

player_row, player_column = player_position()  #запазваме първоначалната позиция на играч
matrix[player_row][player_column] = "."        #затриваме позицията на играча

for command in commands:
    player_movement_row, player_movement_column = player_row + directions[command][0], player_column + directions[command][1]
    if check_valid_position(player_movement_row, player_movement_column, True):
        player_row, player_column = player_movement_row, player_movement_column

    bunny_move(bunny_position())

    if win:
        show_results()

    check_player_alive(player_row, player_column)



# 5 6
# .....P
# ......
# ...B..
# ......
# ......
# ULDDDR
