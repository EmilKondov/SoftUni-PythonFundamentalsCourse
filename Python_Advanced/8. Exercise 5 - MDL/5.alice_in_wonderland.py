size = int(input())

matrix = []
alice_position = []

tea_bags = 0

directions = {
    "up": (-1,0),
    "down": (1,0),
    "left": (0,-1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_position = row, matrix[row].index("A")   # провери дали това остава така или трябва да го запазиш на момент кат олист от два елемента.
        matrix[row][alice_position[1]] = "*"

while tea_bags < 10:
    command = input()
    r, c = alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        break

    alice_position = r, c
    element = matrix[r][c]
    matrix[r][c] = "*"

    if element == "R":
        break

    if element.isdigit():
        tea_bags += int(element)
if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
    
[print(*row, sep=" ") for row in matrix]
