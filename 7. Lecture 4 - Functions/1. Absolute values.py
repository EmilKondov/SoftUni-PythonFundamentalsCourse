sequence_of_numbers = list(map(float, input().split()))

list_of_abs_values = []

for i in sequence_of_numbers:
    list_of_abs_values.append(abs(i))

print(list_of_abs_values)
