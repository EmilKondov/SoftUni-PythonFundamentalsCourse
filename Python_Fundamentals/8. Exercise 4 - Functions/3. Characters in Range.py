def characters_in_range(first, second):
    characters = []
    for current_character in range(ord(first) + 1,ord(second)):
        characters.append(chr(current_character))
    return characters

first_character = input()
second_character = input()
result = characters_in_range(first_character,second_character)
print(" ".join(result))                 # join работи само със стрингове
