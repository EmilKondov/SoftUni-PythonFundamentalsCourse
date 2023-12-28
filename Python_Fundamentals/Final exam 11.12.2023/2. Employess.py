import re

def decrypt_input(input_string):
    pattern = re.compile(
        r"([A-Z][a-z]{2,})\s([A-Z][a-z]{2,})(#*)([A-Z][a-z]+(?:&[A-Z][a-z]+){0,2})\d{2}([A-Z][a-zA-Z0-9]+) (JSC|Ltd\.)")
    match = pattern.match(input_string)

    if match:
        name = f"{match.group(1)} {match.group(2)}"
        position = match.group(4).replace('&', ' ')
        company = f"{match.group(5)} {match.group(6)}"
        return f"{name} is {position} at {company}"


n = int(input())
for employee in range(n):
    input_line = input()
    result = decrypt_input(input_line)
    if result:
        print(result)
