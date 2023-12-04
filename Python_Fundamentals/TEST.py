import sys

smallest = sys.maxsize
biggest = -sys.maxsize
n = int(input())
max_number = 0
min_number = 0

for number in range(n):
    number = int(input())
    if number < smallest:
        smallest = number
    elif number > biggest:
        biggest = number
print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
