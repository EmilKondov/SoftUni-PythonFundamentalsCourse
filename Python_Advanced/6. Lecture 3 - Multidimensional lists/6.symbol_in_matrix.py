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
            location = (row, column)     # Or use directly exit
            found = True

if found:
    print(location)
else:
    print(f"{symbol} does not occur in the matrix")

# Second way - using exit() ####

size = int(input())
matrix = []

for row in range(0, size):
    current_row = [x for x in input()]
    matrix.append(current_row)

symbol = input()
location = ()

for row in range(0, size):
    for column in range(0, size):
        if matrix[row][column] == symbol:
            location = (row, column)     # Or use directly exit
            exit()

print(f"{symbol} does not occur in the matrix")
