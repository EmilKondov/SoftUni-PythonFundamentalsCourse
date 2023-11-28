list_of_numbers = input().split(", ")

positive_numbers = ("Positive:"[int(positive_number) for number in list_of_numbers.split(", ") if number > 0])

print(positive_numbers)