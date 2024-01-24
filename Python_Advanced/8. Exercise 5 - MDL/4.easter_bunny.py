field_size = int(input())
field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

best_path = []                                           # Това са променливите, които ще ми трябват в принта на края на задачата.
total_eggs = float("-inf")                               #  Тези променливи определят и какви променливи ще ми трябват в задачата, като те обаче ще бъдат
best_direction = []                                      #  за отделни цикли или итерации, а накрая всъщност в тези тук ще съхраня финална информация,
                                                         # която и да принитрам.

for row in range(field_size):                            #
    field.append(input().split())                        #
    if "B" in field[row]:                                #
        bunny_pos = [row, field[row].index("B")]         #

    #Here using a for loop I go through the different possible directions and take the new row and col of the bunny
for direction, position in directions.items():
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]
    path = []
    collected_eggs = 0
   # Here I check if the coordinates are valid or not
    while 0 <= row < field_size and 0 <= col < field_size:
        if field[row][col] == "X":
            break

        collected_eggs += int(field[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if collected_eggs >= total_eggs:
        total_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep="\n")
print(total_eggs)



# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0