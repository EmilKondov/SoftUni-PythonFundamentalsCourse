n = 8
for i in range(1, n):
    digit = 1
    for j in range(n, 0, -1):
        if j > i:
            print("", end="")
        else:
            print(digit, end="")
            digit += 1
    print("")