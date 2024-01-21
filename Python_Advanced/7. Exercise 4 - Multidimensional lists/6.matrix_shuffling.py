rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for row in range(rows)]


while True:
    command, *coordinates = input().split()
    coordinates_integers = [int(x) for x in coordinates if int(x) <= rows and int(x) <= columns and int(x) >= 0]


    if command == "END":
        break
    elif command != "swap" or not coordinates_integers or len(coordinates_integers) < 4:
        print(f"Invalid input!")
        continue

    if len(coordinates_integers) == 4:
        r1, c1 = coordinates_integers[:2]
        r2, c2 = coordinates_integers[2:]

        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

        [print(*row) for row in matrix]
