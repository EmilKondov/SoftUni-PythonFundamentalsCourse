first_char_index = int(input())
last_char_index = int(input())
for char in range(first_char_index, last_char_index + 1):
    print(chr(char), end = " ")
