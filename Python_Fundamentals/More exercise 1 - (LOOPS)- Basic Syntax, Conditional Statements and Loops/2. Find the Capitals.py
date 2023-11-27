given_string = input()

list_upper_character = []

for current_character in range(len(given_string)):
  if given_string[current_character].isupper():
    list_upper_character.append(current_character)
  else:
    continue
print(list_upper_character)


### SECOND OPTION USING  ### ENUMERATE INSTEAD range() #####

given_string = input()

list_upper_character = []

for index, character in enumerate(given_string):
  if character.isupper():
    list_upper_character.append(index)

print(list_upper_character)
