size = int(input())
matrix = []

for row in range(size):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
print(sum_diagonal)

#### Second way ###
#
#
# size = int(input())
# matrix = []
#
# for row in range(size):
#     current_row = [int(x) for x in input().split()]
#     matrix.append(current_row)
#
# for row_index in range(size):
#     for col_index in range(size):
#         if row_index == col_index
#