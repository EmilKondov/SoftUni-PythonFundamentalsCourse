size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
coordinates = ((int(x) for x in c.split(",")) for c in input().split())


directions = (
    (-1, 0), #up
    (1, 0),  #down
    (0, -1), #left
    (0, 1),  #right
    (-1, 1),#top right
    (-1, -1),#top left
    (1, -1), # bottom left
    (1, 1), # bottom right
    (0, 0) #current
)


for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue


    for x, y in directions:

        r, c = row + x, col + y

        if 0 <= r < size and 0 <= c < size:         ###  matrix[r][c] -= matrix[row][col] if matric[r][c] > 0 else 0
            if matrix[r][c] > 0:
                matrix[r][c] -= matrix[row][col]
            else:
                matrix[r][c] == 0

alive_cells = [num for row in range(size) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]

