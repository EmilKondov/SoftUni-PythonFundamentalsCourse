#1. Read first line of numbers as a list of numbers
#2. Read the command input
#3.Check if command is != "end"
#4.split the command
#5.create functions

def exchange(numbers, index):
    if index > len(numbers) or index < 0:
        print("Invalid index")
    line_of_numbers = numbers[index:] + numbers[:index]
    print(line_of_numbers)
    return line_of_numbers

def max_even_odd(numbers, even_or_odd):
    if even_or_odd == "even":
        for i in range(len(numbers) -1, -1, -1):
            if numbers[i] % 2 != 0:
                numbers.pop(i)
        numbers.sort()
        print(len(numbers))
        return len(numbers)
    elif even_or_odd == "odd":
        for i in range(len(numbers)):
            if numbers[i] % 2 != 0:
                max_odd_number = numbers[i]
                if max_odd_number < numbers[i + 1]:
                    continue
                else:
                    print(i + 1)
        numbers.sort()
        print(len(numbers))
        return len(numbers)
def min_even():
    pass

def min_odd():
    pass

def firs_even():
    pass

def first_odd():
    pass

def last_even():
    pass

def last_odd():
    pass


line_of_numbers = [int(x) for x in input().split()]
command = input()

while command != "end":
    command = command.split()
    order = command[0]
    if order == "exchange":
        index = int(command[1])
        line_of_numbers = exchange(line_of_numbers, index)
    elif order == "max":
        even_odd = command[1]
        max_number = max_even_odd(line_of_numbers, even_odd)
    elif order == "min":
        even_odd = command[1]
        if even_odd == "even":
            pass
        elif even_odd =="odd":
            pass
    elif order == "first":
        count = command[1]
        even_odd = command[2]
    elif order == "last":
        count = command[1]
        even_odd = command[2]
    command = input()
print(line_of_numbers)

