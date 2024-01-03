#1. Read first line of numbers as a list of numbers
#2. Read the command input
#3.Check if command is != "end"
#4.split the command
#5.create functions

def exchange(numbers, index):
    if index > len(numbers) or index < 0:
        print("Invalid index")
    line_of_numbers = numbers[index:] + numbers[:index]
    return line_of_numbers

def max_even_odd(numbers, even_or_odd):
    if even_or_odd == "even":
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0:
                max_even_number = numbers[i]
                if max_even_number < numbers[i + 1] and numbers[i + 1] != numbers[-1]:
                    continue
                elif numbers[i] != numbers[-1]:
                    max_even_number = i + 1
                    break
                else:
                    max_even_number = i
        return max_even_number
    elif even_or_odd == "odd":
        for i in range(len(numbers)):
            if numbers[i] % 2 != 0:
                max_odd_number = numbers[i]
                if max_odd_number < numbers[i + 1] and numbers[i + 1] != numbers[-1]:
                    continue
                else:
                    max_odd_number = i
                    break
        return max_odd_number
def min_even_odd(numbers, even_or_odd):
    if even_or_odd == "even":
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0:
                min_even_number = numbers[i]
                if min_even_number < numbers[i + 1] and numbers[i + 1] != numbers[-1]:
                    continue
                elif numbers[i] != numbers[-1]:
                    min_even_number = i + 1
                    return min_even_number
                    break
                else:
                    max_even_number = i
                    return max_even_number
                    break
        return "No matches"
    elif even_or_odd == "odd":
        odd_numbers = []
        for i in range(len(numbers)):
            if numbers[i] % 2 != 0 and numbers[i] != 1:
                odd_numbers.append(numbers[i])
            else:
                odd_numbers = "[]"
                return odd_numbers
                break

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
    if order == 'exchange':
        index = int(command[1])
        line_of_numbers = exchange(line_of_numbers, index)
    elif order == "max":
        even_odd = command[1]
        max_number_index = max_even_odd(line_of_numbers, even_odd)
    elif order == "min":
        even_odd = command[1]
        min_number_index = min_even_odd(line_of_numbers, even_odd)
        print(min_number_index)
    elif order == "first":
        count = command[1]
        even_odd = command[2]
    elif order == "last":
        count = command[1]
        even_odd = command[2]
    command = input()

print(line_of_numbers)