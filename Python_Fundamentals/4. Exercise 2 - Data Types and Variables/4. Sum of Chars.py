number_of_lines = int(input())

total_sum_of_ascii_codes = 0

for character in range(number_of_lines):
    current_character = input()
    value_of_current_character = ord(current_character)
    total_sum_of_ascii_codes += value_of_current_character
print(f"The sum equals: {total_sum_of_ascii_codes}")
