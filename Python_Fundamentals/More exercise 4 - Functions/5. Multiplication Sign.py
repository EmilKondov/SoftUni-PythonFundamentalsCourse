n = 3
counter = 0
numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)
    if number < 0:
        counter += 1

if 0 in numbers:
    print("zero")
elif counter % 2 == 0:
    print("positive")
else:
    print("negative")
