#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#for i in range(len(matrix)):
#    for j in range(len(matrix[i])):
#        print(matrix[i][j], end=" ")
#    print()



def print_row(size, star_count):
    for row in range(size - star_count):
        print(" ", end="")
    for row in range(1 - size):
        print("*", end="")
    print("*")

size = int(input())
for star_count in range(1, size):
    print_row(size, star_count)

for star_count in range(size, 0 , -1):
    print_row(size, star_count)