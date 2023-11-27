number_n = int(input())

for i in range(0, number_n):
    for j in range(0, number_n):
        for l in range(0, number_n):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + l)}")
