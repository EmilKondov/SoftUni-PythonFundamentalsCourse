def smallets_number(some_number):
    min_element = min(some_number)
    return (min_element)

num1 = int(input())
num2 = int(input())
num3 = int(input())

list_of_numbers = [num1, num2, num3]
print(smallets_number(list_of_numbers))
