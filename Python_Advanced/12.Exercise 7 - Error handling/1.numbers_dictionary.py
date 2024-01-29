numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number
    line = input()

while line != "Remove":
    searched = line
    searched_numbers_as_text = input()
    try:
        print(numbers_dictionary[searched_numbers_as_text])
    except KeyError:
        print(numbers_dictionary)
    line = input()

while line != "End":
    searched = line
    searched_text_number = input()
    try:
        del numbers_dictionary[searched_text_number]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()
print(numbers_dictionary)