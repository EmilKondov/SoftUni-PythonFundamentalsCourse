def sum_numbers(first, second):
    return first + second

def subtract(sum, third_number):
    return sum - third_number

def add_and_subtract(fist, second, third):
    sum_of_first_and_second_number = sum_numbers(fist, second)
    result = subtract(sum_of_first_and_second_number, third)
    return result
    

first_number = int(input())
second_number = int(input())
thrid_number = int(input())
print(add_and_subtract(first_number, second_number, thrid_number))




