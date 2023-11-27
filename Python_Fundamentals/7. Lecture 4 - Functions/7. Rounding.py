list_of_numbers = list(map(float, input().split()))

list_of_rounded_numbers = []

for i in list_of_numbers:
    list_of_rounded_numbers.append(round(i))

print(list_of_rounded_numbers)
