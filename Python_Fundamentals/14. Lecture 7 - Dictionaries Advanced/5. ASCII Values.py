list_of_characters = input().split(', ')
characters_dict = {key: ord(key) for key in list_of_characters}

print(characters_dict)