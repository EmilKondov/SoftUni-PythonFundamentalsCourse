MAX_SIZE = 4
people_waiting = int(input())
lift = [int(x) for x in input().split()]

for i in range(len(lift)):
    free_spaces = MAX_SIZE - lift[i]

    if people_waiting >= free_spaces:
        lift[i] += free_spaces
    else:
        lift[i] += people_waiting
    people_waiting -= free_spaces
    if people_waiting <= 0 and (i != len(lift) -1 or lift[i] < MAX_SIZE):
        print(f"The lift has empty spots!")
        break
else:
    if people_waiting > 0:
        print(f"There isn't enough space! {people_waiting} people in a queue!")
print(*lift)
