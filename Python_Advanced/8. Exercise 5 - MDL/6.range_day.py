from typing import List

def move(direction, steps):

    """В тази функция се преместваме на зададена позиция и едновременно
    проверяваме дали тези координати са валидни(се намират в матрицата, а не извън нея)
    """

    r = shooter_position[0] + directions[direction][0] * steps
    c = shooter_position[1] + directions[direction][1] * steps

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return shooter_position
    if matrix[r][c] == "x":
        return shooter_position

    return [r, c]

def shoot(direction): # чрез pipe( | ) обозначаваме, че ще ни върне едноито или другото.
    """
    Тази функцкия ще ни връща координатите на мишената, която сме уцелили.
    """
    r = shooter_position[0] + directions[direction][0]
    c = shooter_position[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]

# Initial data from the console
SIZE = 5  # константни променливи пишем с главни букви
matrix = []

total_targets = 0
shot_targets = 0

shooter_position = []
targets_positions = []

directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}
for row in range(SIZE):
    matrix.append(input().split())

    if "x" in matrix[row]:
        total_targets += matrix[row].count("x")

    if "A" in matrix[row]:
        shooter_position = [row, matrix[row].index("A")]

#Logic
for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == "move":
        shooter_position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        target_position = shoot(command_info[1])

        if target_position:
            targets_positions.append(target_position)
            shot_targets += 1

        if total_targets == shot_targets:
            print(f"Training completed! All {shot_targets} targets hit.")
            break

if total_targets > shot_targets:
    print(f"Training not completed! {total_targets - shot_targets} targets left.")

print(*targets_positions, sep="\n")
