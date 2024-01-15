# string_input = input()
# list_of_the_string = [character for character in string_input]
# input_characters = {}
#
# for character in string_input:
#     input_characters[character] = list_of_the_string.count(character)
#
# for char, count in sorted(input_characters.items()):
#     print(f"{char}: {count} time/s")
#
#
# ### Second solution ###
#
#
# occurences = {}
#
# for symbol in input():
#     occurences[symbol] = occurences.get(symbol, 0 ) + 1
#
# for letter, occurence in sorted(occurences.items()):  # (("a", 1), ("b", 3)) sorted returns us a tuple.
#     print(f"{letter}: {occurence} time/s")
#

### Third solution ###

text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")
