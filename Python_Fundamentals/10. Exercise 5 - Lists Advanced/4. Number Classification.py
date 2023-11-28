list_of_numbers = input().split(", ")

positive = [number for number in list_of_numbers if int(number) >= 0]
print(positive)