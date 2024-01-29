# rows, columns = [int(x) for x in input().split()]
# matrix = [[x for x in input().split()] for row in range(rows)]
#
#
# while True:
#     command, *coordinates = input().split()
#
#     if command == "END":
#         break
#     elif command != "swap" or not coordinates or len(coordinates) != 4:
#         print(f"Invalid input!")
#         continue
#
#     coordinates_integers = [int(x) for x in coordinates]
#     r1, c1, r2, c2 = coordinates_integers
#
#     if not (0 <= r1 < rows and 0 <= c1 < columns and 0 <= r2 < rows and 0 <= c2 < columns):
#         print(f"Invalid input!")
#         continue
#
#     matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
#
#     [print(*row) for row in matrix]

# Second more advanced solution

def check_indices(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def swap_items(command_type, indices):
    if len(indices) == 4 and check_indices(indices) and command == "swap":
        r1, c1, r2, c2 = indices
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

        [print(*row) for row in matrix]

    else:
        print("Invalid input!")

rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(columns)

while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    swap_items(command, coordinates)
    check_indices(coordinates)


# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END