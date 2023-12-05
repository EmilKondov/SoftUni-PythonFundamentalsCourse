int_numbers = input().split()
given_string = input()


message = []

for number in int_numbers:
    lenght_of_string = len(given_string)
    sum_of_number = 0
    for digit in number:
        sum_of_number += int(digit)
    if sum_of_number >= lenght_of_string:
        sum_of_number -= lenght_of_string
    message.append(given_string[sum_of_number])
    given_string = given_string[:sum_of_number] + given_string[sum_of_number + 1:]
print("".join(message))
