sequence_of_strings = input().split()
total_sum = 0
for given_string in sequence_of_strings:
    first_letter = given_string[0]
    last_letter = given_string[-1]
    current_number = int(given_string[1:-1])
    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += current_number / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += current_number * first_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position
print(f"{total_sum:.2f}")
