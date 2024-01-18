rows = int(input())

matrix_elements = []

for row in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix_elements.extend(current_row)
print(matrix_elements)
