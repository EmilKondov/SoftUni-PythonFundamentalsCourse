given_string = input()

list_upper_character = []

for current_character in range(len(given_string)):
  if given_string[current_character].isupper():
    list_upper_character.append(current_character)
  else:
    continue
print(list_upper_character)
