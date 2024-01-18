rows = int(input())

matrix_elements = []

for row in range(rows):
    current_row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix_elements.append(current_row)
print(matrix_elements)
