import sys

line_of_numbers = [int(x) for x in input().split()]
command = input().split()
mutated_line = []

while command[0] != 'end':
    even_numbers = [int(even) for even in line_of_numbers if even % 2 == 0]
    odd_numbers = [int(odd) for odd in line_of_numbers if odd % 2 !=0]
    max_number = -sys.maxsize
    min_number = sys.maxsize
    value_index = 0
    is_found = False
    counter = 0
    first_even = []
    first_odd = []
    last_even = []
    last_odd = []

    if command[0] == "exchange":
        index = int(command[1])
        if index > len(line_of_numbers) or index < 0:
            print("Invalid index")
        else:
            mutated_line = line_of_numbers[index + 1:] + line_of_numbers[:index + 1]
            line_of_numbers = mutated_line
    elif command[0] == "max":
        if "even" in command[1]:
            for index, value in enumerate(line_of_numbers):
                if value % 2 == 0:
                    if value >= max_number:
                        max_number = value
                        value_index = index
                        is_found = True
        else:
            for index, value in enumerate(line_of_numbers):
                if value % 2 != 0:
                    if value >= max_number:
                        max_number = value
                        value_index = index
                        is_found = True
        if is_found:
            print(value_index)
        else:
            print("No matches")

    elif command[0] == "min":
        if "even" in command[1]:
            for index, value in enumerate(line_of_numbers):
                if value % 2 == 0:
                    if value <= min_number:
                        min_number = value
                        value_index = index
                        is_found = True
        elif "odd" in command[1]:
            for index, value in enumerate(line_of_numbers):
                if value % 2 != 0:
                    if value <= min_number:
                        min_number = value
                        value_index = index
                        is_found = True
        if is_found:
            print(value_index)
        else:
            print("No matches")

    elif command[0] == "first":
        current_count, even_odd = command[1],command[2]
        if even_odd == "even":
            for index, value in enumerate(even_numbers):
                if index < int(current_count):
                    first_even.append(value)
        else:
            for index, value in enumerate(odd_numbers):
                if index < int(current_count):
                    first_odd.append(value)
                    is_found = True
                else:
                    break
        if is_found and even_odd == "even":
            print(first_even)
        elif is_found and even_odd == "odd":
            print(first_odd)

    elif command[0] == "last":
        current_count, even_odd = int(command[1]), command[2]
        if int(current_count) > len(line_of_numbers):
            print("Invalid count")
        if even_odd == "even":
            print(even_numbers[-current_count:])
        else:
            if int(current_count) > len(line_of_numbers):
                print("Invalid count")
            else:
                print(odd_numbers[-current_count:])
    command = input().split()
print(line_of_numbers)
