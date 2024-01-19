size = int(input())
matrix = [list(map(int, input().split())) for x in range(size)]

principal_diagonal = []
secondary_diagonal = []


for row in range(size):
    for col in range(size):

        if row == col:
            principal_diagonal.append(matrix[row][col])

        if ((row + col) == (size - 1)):
            secondary_diagonal.append(matrix[row][col])

print(abs(sum(principal_diagonal) - sum(secondary_diagonal)))




# 3
# 11 2 4
# 4 5 6
# 10 8 -12

