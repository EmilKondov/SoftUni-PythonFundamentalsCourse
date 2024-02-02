class InvalidColumnChoice(Exception):
    pass
class FullColumnError(Exception):
    pass

ROWS = 6
COLUMNS = 7

#Functions
def print_board(board):
    for row in board:
        print(row)


def validate_column_choice(column):
    if 1 <= column < COLUMNS:
        return True
    return InvalidColumnChoice

def get_first_available_row(col_index, board):
    for row in range(ROWS -1, -1, -1):
        if board[row][col_index] == 0:
            return row
    else:
        raise FullColumnError

def travel_direction(coordinates, board)

def is_winner(current_row_index, current_col_index, board):
    for direction, coords in DIRECTIONS.items():
        searched_element = board[current_row_index][current_col_index]
        travel_direction(coords, searched_element, board)
#Initial input
board = []
for _ in range(ROWS):
    board.append([0] * COLUMNS)


DIRECTIONS = {
    "left": (0, -1),
    "up": (-1, 0),
    "primary_diagonal": (-1, -1),
    "secondary_diagonal": (-1, 1)
}


turn = 1

while True:
    player = 2 if turn % 2 == 0 else 1

    try:
        column = int(input(f"Player {player}, please choose a columns "))
        validate_column_choice(column)
        column_index = int(column) - 1
        row = get_first_available_row(column_index, board)
        board[row][column_index] = player
        if is_winner(row, column_index, board):
            break
    except FullColumnError as ex:
        print(f"This column is full, please select another one")
        continue
    except (InvalidColumnChoice, ValueError):
        print(f"This column is invalid, please select a number between 1 and {COLUMNS}")
        continue

    print_board(board)
    turn += 1
print(f"WINNER is {player}")
print_board(board)