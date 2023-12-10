import re
pattern = "\\+359-2-\\d{3}-\\d{4}\\b|\\+359 2 \\d{3} \\d{4}\\b"
numbers = input()
matches = re.findall(pattern, numbers)
print(", ".join(matches))
