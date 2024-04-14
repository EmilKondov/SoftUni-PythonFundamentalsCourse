import re

pattern = r"[A-Z][a-z]{2,}\s[A-Z][a-z]{2,}##[A-Z][a-z]*(?:&[A-Z][a-z]*){0,2}\d{2}[A-Z][a-zA-Z0-9]*\s(JSC|Ltd\.)$"

n = int(input())

for _ in range(n):
    row_data = input()

    if re.match(pattern, row_data):
        print(f"{employee name} is {job position} at {company name}")
