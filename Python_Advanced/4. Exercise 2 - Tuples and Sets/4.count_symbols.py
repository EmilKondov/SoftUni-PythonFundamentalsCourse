string_input = input()
list_of_the_string = [character for character in string_input]
input_characters = {}

for character in string_input:
    input_characters[character] = list_of_the_string.count(character)

for char, count in sorted(input_characters.items()):
    print(f"{char}: {count} time/s")
