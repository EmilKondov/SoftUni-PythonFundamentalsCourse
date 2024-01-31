size = int(input())

matrix = [list(input()) for row in range(size)]

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

    knight_with_most_attacks = []
    max_attacks= 0

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                atacks = 0

                for coordinates in possitions:
                    r, c = row + coordinates[0], col + coordinates[1]


                    if 0 <= r < size and 0 <= c < size:
                        if matrix[r][c] == "K":
                            atacks += 1

                if atacks > max_attacks:
                    knight_with_most_attacks = [row, col]
                    max_attacks = atacks

    if knight_with_most_attacks:
        r, c = knight_with_most_attacks
        matrix[r][c] = 0
        removed_knights += 1
    else:
        break

print(removed_knights)
