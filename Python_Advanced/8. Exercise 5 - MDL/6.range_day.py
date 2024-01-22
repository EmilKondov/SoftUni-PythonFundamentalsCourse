rows, columns = 5, 5
matrix = [[x for x in input().split()] for x in range(rows)]
count_of_commands = int(input())

for command in range(count_of_commands):
    




def my_initail_position(matrix):
    for row in matrix:
        if "A" in row:
            return row, matrix[row].index("A")


my_row, my_col = my_initail_position(matrix)
print(my_row, my_col)





# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x