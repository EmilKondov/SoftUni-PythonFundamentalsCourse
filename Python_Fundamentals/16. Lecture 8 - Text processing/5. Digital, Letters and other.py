single_string = input()

numbers = ""
text = ""
special_symbols = ""
for digit in single_string:
    if digit.isdigit():
        numbers += str(digit)
    elif not digit.isdigit() and digit.isalnum():
        text += digit
    else:
        special_symbols += digit

print(numbers)
print(text)
print(special_symbols)
