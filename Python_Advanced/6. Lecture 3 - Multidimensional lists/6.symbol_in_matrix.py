size = int(input())
matrix = []

for row in range(0, size):
    current_row = [x for x in input()]
    matrix.append(current_row)

symbol = input()
location = ()
found = False

for row in range(0, size):
    if found:
        break
    for column in range(0, size):
        if matrix[row][column] == symbol:
            location = (row, column)
            found = True

if found:
    print(location)
else:
    print(f"{symbol} does not occur in the matrix")
