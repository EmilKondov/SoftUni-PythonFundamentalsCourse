rows, columns = [int(x) for x in input().split(",")]

matrix = []

for row in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)

print(submatrix_square(matrix))