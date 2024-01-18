rows, columns = [int(x) for x in input().split(", ")]

matrix_elements = []
sum = 0

for row in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix_elements.append(current_row)

for element in matrix_elements:
    for number in element:
        sum += number

print(sum)
print(matrix_elements)
