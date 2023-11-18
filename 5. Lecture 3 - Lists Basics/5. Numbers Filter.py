#given_number_n = int(input())
#
#list_of_numbers = []
##list_of_commands = ["even", "odd", "negative", "positive"]
#
#for current_number in range(given_number_n):
#    current_number = int(input())
#    list_of_numbers.append(current_number)
#
#command = input()
#filtered_numbers = []
#if command == "even":
#    for num in list_of_numbers:
#        if num % 2 == 0:
#            filtered_numbers.append(num)
#elif command == "odd":
#    for num in list_of_numbers:
#        if num % 2 != 0:
#            filtered_numbers.append(num)
#elif command == "negative":
#    for num in list_of_numbers:
#        if num < 0:
#            filtered_numbers.append(num)
#elif command == "positive":
#    for num in list_of_numbers:
#        if num >= 0:
#            filtered_numbers.append(num)
#
#print(filtered_numbers)
#

##############  SECOND WAY ####################


n =int(input())

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

list_of_numbers = [int(input()) for _ in range(n)]
filtered_numbers = []

command = input()

for num in list_of_numbers:
    filter_command = (
        (command == COMMAND_EVEN and num % 2==0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_NEGATIVE and num < 0) or
        (command == COMMAND_POSITIVE and num > 0)
        )

    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)