number = int(input())
tribonacci = []

for i in range(number):
    if i == 0:
        tribonacci.append(1)
    elif i == 1:
        tribonacci.append(tribonacci[0])
    elif i == 2:
        tribonacci.append(tribonacci[0] + tribonacci[1])
    else:
        tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])

print(*tribonacci)
