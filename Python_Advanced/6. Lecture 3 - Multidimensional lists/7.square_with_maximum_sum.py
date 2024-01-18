rows, columns = [int(x) for x in input().split(",")]


def submatrix_square(matrix):
    s = []  # stands for auxiliary matrix
    for i in range(rows):
        temp = []
        for j in range(columns):
            if i == 0 or j == 0:
                temp.append(matrix[i][j])
            else:
                temp.append(0)
        s.append(temp)

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 1:
                s[i][j] = min(s[i][j-1], s[i-1][j], s[i-1][j-1]) + 1

            else:
                s[i][j] = 0


    max_of_s = s[0][0]

    max_i = 0
    max_j = 0

    for i in range(rows):
        for j in range(columns):
            if max_of_s < s[i][j]:
                max_of_s = s[i][j]
                max_i = i
                max_j = j

    # Maximum size sub-matrix is :

    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j - max_of_s, -1):
            print(matrix[i][j], end=" ")
        print("")

matrix = []

for row in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)

print(submatrix_square(matrix))