n = int(input())
count_of_solutions = 0

for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            sum = x1 + x2 + x3
            if sum == n:
                count_of_solutions += 1
print(count_of_solutions)
