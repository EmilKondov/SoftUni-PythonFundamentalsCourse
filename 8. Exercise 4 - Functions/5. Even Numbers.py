#def is_even(number):
#    if number % 2 ==0:
#        return number
#
#list_of_numbers = list(map(int, input().split()))
#result = list(filter(is_even, list_of_numbers))
#print(result)
#
#


##### SECOND WAY ####


def is_even(number):
    if number % 2 ==0:
        return number

numbers_as_string = input().split()
numbers_as_int = []

for current_number in numbers_as_string:
    numbers_as_int.append(int(current_number))
result = list(filter(is_even, numbers_as_int))
print(result)
