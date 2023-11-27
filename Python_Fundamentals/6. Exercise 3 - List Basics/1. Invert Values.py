list_of_numbers = input().split()

oposite_numbers = []

for element in list_of_numbers:
    current_number = -int(element)
    oposite_numbers.append(current_number)
print(oposite_numbers)
