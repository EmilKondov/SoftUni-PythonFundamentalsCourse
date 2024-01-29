numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    number = int(input())
    numbers_dictionary[number_as_string] = number
    line = input()

while line != "Remove":
    searched = line
    searched_numbers_as_text = input()
    print(numbers_dictionary[searched_numbers_as_text])
    line = input()

while line != "End":
    searched = line
    searched_text_number = input()
    del numbers_dictionary[searched_text_number]
    line = input()
print(numbers_dictionary)










# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End