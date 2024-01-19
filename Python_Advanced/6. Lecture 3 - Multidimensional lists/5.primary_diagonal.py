size = int(input())
matrix = []

for row in range(size):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))

for i in range(size - 1):
    for j in range(size -1):
        lower = matrix[i + 2][i]
        central = matrix[i + 1][j + 1]
        upper = matrix[i][j + 2]
        sum_second_diagonal = lower + central + upper
        break

print(sum_diagonal)
print(sum_second_diagonal)






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
