size = int(input())
matrix = [[int(x) for x in input().split(", ")] for x in range(size)]

principal_diagonal = []
secondary_diagonal = []

for row in range(size):
    for col in range(size):

        if row == col:
            principal_diagonal.append(matrix[row][col])

        if ((row + col) == (size - 1)):
            secondary_diagonal.append(matrix[row][col])


print(f"Primary diagonal: {', '.join([str(x) for x in principal_diagonal])}. Sum: {sum(principal_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(y) for y in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")




# for i in range(size):
#     for j in range(size):
#         if ((i + j) == (size - 1)):
#             secondary_diagonal.append(matrix[i][j])




#primary_diagonal_sum = sum(matrix[size - i - 1][size - i - 1] for i in range(size))

