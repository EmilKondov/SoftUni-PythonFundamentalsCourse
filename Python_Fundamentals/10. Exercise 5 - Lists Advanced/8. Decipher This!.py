secret_message = input().split()
for word in secret_message:
    list_of_numbers = []
    list_of_letters = []
    for character in word:
        if character.isdigit():
            list_of_numbers.append(character)
        elif character.isalpha():
            list_of_letters.append(character)
    first_letter = chr(int("".join(list_of_numbers)))
    list_of_letters[0], list_of_letters[-1] = list_of_letters [-1], list_of_letters[0]
    letters_after_first = "".join(list_of_letters)
    deciphered_word = first_letter + letters_after_first
    print(deciphered_word, end=" ")