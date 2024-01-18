size = int(input())
matrix = [[int(x) for x in input().split(", ")] for x in range(size)]


primary_diagonal_sum = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
(matrix[size - i - 1] for i in range(size))
(matrix[size - i - 1] for i in range(size -1, -1, -1))

print(list1)
print(list2)
#secondary_diagonal_sum = sum(matrix[size - i - 1][size - i - 1] for i in range(size))


# [3 - 0 - 1][3 - 0 - 1] = 9
# [3 - 1 - 1][3 - 1 - 1] = 5
# [3 - 2 - 1][3 - 2 - 1]  = 1
#
# [3 - 0 - 1][3 - 2 - 1] = 7
# [3 - 1 - 1][3 - 1 - 1] = 5
# [3 - 2 - 1][3 - 0 - 1] = 3

