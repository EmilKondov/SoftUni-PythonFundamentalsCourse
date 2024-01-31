size = int(input()) # прочитаме размера на матрицата

matrix = [[int(x) for x in input().split()] for row in range(size)] # прочитаме си входните дани за матрица и образуваме матрица от числа.

command = input().split() # разделяме входните дани от конзолата в лист

while command[0] != "END": # Проверяваме дали е различно от END, ако е развъртаме цикъл.
    action, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3]) #

    if 0 <= row < size and 0 <= col < size:

        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value

    else:
        print("Invalid coordinates")

    command = input().split()

[print(*row) for row in matrix]
