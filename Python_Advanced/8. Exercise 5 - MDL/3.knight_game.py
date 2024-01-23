size = int(input())
board = [list(input()) for _ in range(size)]

possitions = (
     (-2, -1),
     (-2, 1),
     (-1, -2),
     (-1, 2),
     (2, 1),
     (2, -1),
     (1, -2),
     (1, 2),
)
removed_knights = 0
while True:
    max_attacks = 0
    knights_with_most_attacks = []

    for row in range(size):
        for col in range(size):
            if board[row][col] == "K":
                attacks = 0

                for pos in possitions:
                    for_row = row + pos[0]
                    for_col = col + pos[1]

                    if 0 <= for_row < size and 0 <= for_col < size:
                        if board[for_row][for_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knights_with_most_attacks = [row, col]
                    max_attacks = attacks
    if knights_with_most_attacks:
        r, c = knights_with_most_attacks
        board[r][c] = 0
        removed_knights += 1
    else:
        break
        
print(removed_knights)
