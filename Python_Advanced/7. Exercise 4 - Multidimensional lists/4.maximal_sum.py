rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]
sub_matrix = []
current_row = []

for row in range(3):
    for column in range(3):
        current_row.append(matrix[row][column])
    sub_matrix.append(current_row)