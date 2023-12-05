given_integers = input().split(", ")

for number in range(len(given_integers) -1, -1, -1):
    if int(given_integers[number]) == 0:
        given_integers.insert(len(given_integers), given_integers.pop(number))
print([int(i) for i in given_integers])
