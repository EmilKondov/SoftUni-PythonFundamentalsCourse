# rows, columns = [int(x) for x in input().split(", ")]
#
# matrix_elements = []
# sum = 0
#
# for row in range(rows):
#     current_row = [int(x) for x in input().split(", ")]
#     matrix_elements.append(current_row)
#
# for element in matrix_elements:
#     for number in element:
#         sum += number
#
# print(sum)
# print(matrix_elements)


### Second solution###

rows, columns = [int(x) for x in input().split(", ")]

total_amount = 0
matrix_elements = []


for row in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    total_amount += sum(current_row)
    matrix_elements.append(current_row)


print(total_amount)
print(matrix_elements)
