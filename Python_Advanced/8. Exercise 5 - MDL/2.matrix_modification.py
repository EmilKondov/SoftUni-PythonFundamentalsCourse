rows = int(input())

def valid_coordinates(row, col):
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix) -1:
        return True
    else:
        print("Invalid coordinates")



matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command, *numbers = input().split()

    if command == "END":
        break

    row, col, value = [int(x) for x in numbers]

    if valid_coordinates(row, col):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value

for row in matrix:
    print(*row)







# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END