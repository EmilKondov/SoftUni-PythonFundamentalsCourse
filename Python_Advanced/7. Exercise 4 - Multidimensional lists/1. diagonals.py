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
