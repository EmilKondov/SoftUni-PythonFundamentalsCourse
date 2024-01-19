rows, cols = [int(x) for x in input().split(",")]

matrix = []

for row in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)

max_sum = float('-inf')
sub_matrix = []


for row_index in range(rows - 1):                              # 5, 5
    for col_index in range(cols - 1):                          # 7, 1, 3, 9, 9
        first_left = matrix[row_index][col_index]              # 1, 3, 9, 8, 9
        second_right = matrix[row_index][col_index + 1]        # 4, 9, 8, 9, 1
        down_left = matrix[row_index + 1][col_index]           # 9, 9, 4, 6, 9
        down_right = matrix[row_index + 1][col_index +1]       # 7, 9, 5, 4, 2

        current_sum = first_left + second_right + down_left + down_right

        if max_sum < current_sum:
            max_sum = current_sum
            sub_matrix = [[first_left, second_right], [down_left, down_right]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)

# 6, 6
# 7, 1, 3, 9, 9, 8
# 1, 3, 9, 8, 9, 7
# 4, 9, 8, 9, 1, 4
# 9, 9, 4, 6, 9, 5
# 7, 9, 5, 4, 2, 2
# 6, 9, 8, 3, 1, 4