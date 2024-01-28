def move(command: str):
    r = santa_position[0] + directions[command][0]
    c = santa_position[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        return santa_position

    return [r, c]

def eat_cookie(remaining_presents: int, nice_kids: int):
    for coordinates in directions.values():
        r = santa_position[0] + coordinates[0]
        c = santa_position[1] + coordinates[1]

        if neighbourhood[r][c].isalpha():
            if neighbourhood[r][c] == "V":
                nice_kids += 1

            neighbourhood[r][c] = "-"
            remaining_presents -= 1

        if not remaining_presents:
            break
    return remaining_presents, nice_kids


count_of_presents = int(input())
size = int(input())

neighbourhood = []
santa_position = []

total_nice_kids = 0
nice_kids_visited = 0

directions = {
    "up": (-1,0),
    "down": (1,0),
    "left": (0,-1),
    "right": (0, 1)
}


for row in range(size):
    neighbourhood.append(input().split())

    if "S" in neighbourhood[row]:
        santa_position = [row, neighbourhood[row].index("S")]
        neighbourhood[row][santa_position[1]] = "-"

    if "V" in neighbourhood[row]:
        total_nice_kids += 1

command = input()
while command != "Christmas morning":

    santa_position = move(command)
    house = neighbourhood[santa_position[0]][santa_position[1]]

    if house == "V":
        nice_kids_visited += 1
        count_of_presents -= 1

    elif house == "C":
        count_of_presents, nice_kids_visited = eat_cookie(count_of_presents, nice_kids_visited)

    neighbourhood[santa_position[0]][santa_position[1]] = "-"

    if not count_of_presents or nice_kids_visited == total_nice_kids:
        print("Santa ran out of presents!")

    command = input()

neighbourhood[santa_position[0]][santa_position[1]] = "S"

if not count_of_presents and nice_kids_visited < total_nice_kids:
    print("Santa tun out of presents!")
[print(*row) for row in neighbourhood]

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")