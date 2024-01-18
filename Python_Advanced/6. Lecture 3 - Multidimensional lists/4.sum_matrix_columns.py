from collections import deque
rows, columns = [int(x) for x in input().split(", ")]

matrix = []
traverse_matrix_elements = []

for row in range(rows):
    current_row = deque([int(x) for x in input().split()])
    matrix.append(current_row)

result = []

for i in range(columns):
    column_sum = 0
    new_row = []
    for j in range(rows):
        column_sum += matrix[j][i]
        new_row.append(matrix[j][i])
    result.append(column_sum)
    traverse_matrix_elements.append(new_row)
[print(x) for x in result]
