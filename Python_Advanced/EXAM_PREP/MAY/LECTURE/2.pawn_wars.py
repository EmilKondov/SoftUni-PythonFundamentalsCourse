SIZE = 8

matrix = []
white_pawn_pos = []
black_pawn_pos = []

for row in range(SIZE):
    matrix.append(input().split())

    if "b" in matrix[row]:
        black_pawn_pos = [row, matrix[row].index("b")]

    if "w" in matrix[row]:
        white_pawn_pos = [row, matrix[row].index(("w"))]

    #трябва да сложиш "-" на съответната позиция


while white_pawn_pos[0] > 0 and black_pawn_pos[0] <= SIZE:

    if not (white_pawn_pos[1] - 1 == black_pawn_pos[1] or white_pawn_pos[1] + 1 == black_pawn_pos[1]):
        black_pawn_pos[0] += 1
        white_pawn_pos[0] -= 1


    



if white_pawn_pos[0] == 0:
    print(f"Game over! White pawn is promoted to a queen at {white_pawn_pos}.")
else:
    print(f"Game over! Black pawn is promoted to a queen at {black_pawn_pos}.")


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
chess_board = []


for char in alphabet:
    for num in range(1, SIZE + 1):
        chess_board.append(f"{(char + num)}")
    print()