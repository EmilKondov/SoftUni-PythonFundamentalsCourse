def valid_position(current_row, current_column):
    if 0 <= current_row < rows and 0 <= current_column < cols:
        return True
    else:
        return False

rows, cols = [int(x) for x in input().split(",")]
matrix = []

mouse_position = []
total_cheese = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
for row in range(rows):
    matrix.append(list(input()))

    if "M" in matrix[row]:
        mouse_position = [row, matrix[row].index("M")]
        matrix[row][matrix[row].index("M")] = "*"

    if "C" in matrix[row]:
        total_cheese += matrix[row].count("C")

while total_cheese:
    command = input()

    if command == "danger" and total_cheese:
        print("Mouse will come back later!")
        exit()

    row = mouse_position[0] + directions[command][0]
    col = mouse_position[1] + directions[command][1]

    if valid_position(row, col):
        if matrix[row][col] == "@":
            continue                  
        if matrix[row][col] == "*":
             mouse_position = [row, col]
        elif matrix[row][col] == "C":
            total_cheese -= 1
            mouse_position = [row, col]

            if total_cheese == 0:
                matrix[row][col] = "M"
                print("Happy mouse! All the cheese is eaten, good night!")
                break
            else:
                matrix[row][col] = "*"
        elif matrix[row][col] == "T":
            matrix[row][col] = "M"
            print("Mouse is trapped!")
            break
    else:
        matrix[mouse_position[0]][mouse_position[1]] = "M"
        print("No more cheese for tonight!")
        break
[print(*row, sep="") for row in matrix]
