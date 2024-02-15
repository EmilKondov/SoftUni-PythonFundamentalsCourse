### Input

size =int(input())

matrix = []
gambler_position = []

initial_amount = 100
total_amount = initial_amount

jackpot_win = False
#дефинираме посоки
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
#прочитаме матрицата
for row in range(size):
    matrix.append(list(input()))
    #намираме, запазвам и премахваме символа от позицията на играча

    if "G" in matrix[row]:
        gambler_position = [row, matrix[row].index("G")]
        matrix[row][matrix[row].index("G")] = "-"



### Logic

direction = input()

while direction != "end":

    gambler_next_row = gambler_position[0] + directions[direction][0]
    gambler_next_col = gambler_position[1] + directions[direction][1]

    if not (0 <= gambler_next_row < size and 0 <= gambler_next_col < size) or total_amount <= 0:
        print("Game over! You lost everything!")
        break

    r, c = gambler_next_row, gambler_next_col
    gambler_position = [r, c]
    # трябва да сложиш "-", където е минал

    if matrix[r][c] == "J":
        total_amount += 100000
        matrix[r][c] = "G"
        print(f"You win the Jackpot!\n"
              f"End of the game. Total amount: {total_amount}$")
        jackpot_win = True
        break

    #тук проверяваме всички случаи, които не прекратяват играта
    else:
        if matrix[r][c] == "-":
            continue
        elif matrix[r][c] == "W":
            total_amount += 100
        elif matrix[r][c] == "P":
            total_amount -= 200

    matrix[r][c] = "-"
    direction = input()


if jackpot_win:
    print(f"End of the game. Total amount: {total_amount}$")
    [print(*row) for row in matrix]

# 4
# G---
# WWWW
# P---
# PJ--
# right
# right
# right
# down
# left
# left
# end


# 4
# ---G
# W-W-
# ---P
# --JW
# left
# down
# down
# down
# right
# end