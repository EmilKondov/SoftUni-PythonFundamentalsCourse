size = int(input())

matrix = []
alice_position = []
total_tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]
        matrix[row][matrix[row].index("A")] = "*"



while total_tea_bags < 10:
    command = input()
    r, c = alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]

    if 0 <= r < size and 0 <= c < size:
        alice_position = [r, c]

        if matrix[r][c].isdigit():
            total_tea_bags += int(matrix[r][c])


        elif matrix[r][c] == "R":
            print("Alice didn't make it to the tea party.")
            matrix[r][c] = "*"
            break

    else:
        print("Alice didn't make it to the tea party.")
        break
    matrix[r][c] = "*"

else:
    print(f"She did it! She went to the party.")

[print(*row) for row in matrix]
