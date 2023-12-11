key = int(input())
number_of_lines = int(input())
message = []

for value in range(number_of_lines):
    value = ord(input()) + key
    message.append(chr(value))
print("".join(message))

