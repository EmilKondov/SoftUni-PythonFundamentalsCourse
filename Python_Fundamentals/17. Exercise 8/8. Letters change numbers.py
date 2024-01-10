sequence_of_strings = input().split()
total_sum = 0
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for text in sequence_of_strings:
    current_string = text
    if current_string[0].isupper():
        number = current_string[1:-1]
        for i in range(len(alphabet)):
            if alphabet[i] == current_string[0]:
                divisor = int(i + 1)
                number = int(number) // divisor
                total_sum += number
    elif current_string[0].islower():
        number = current_string[1:-1]
        for i in range(len(alphabet)):
            if alphabet[i].lower() == current_string[0]:
                divisor = int(i + 1)
                number = int(number) * divisor
                total_sum += number

    if current_string[-1].isupper():
        number = current_string[1:-1]
        for i in range(len(alphabet)):
            if alphabet[i] == current_string[-1]:
                substracting_number = int(i + 1)
                number = int(number) - substracting_number
                total_sum += number
    elif current_string[-1].islower():
        number = current_string[1:-1]
        for i in range(len(alphabet)):
            if alphabet[i].lower() == current_string[-1]:
                adding_number = int(i + 1)
                number = int(number) + adding_number
                total_sum += number
print(total_sum)
