number_of_lines = int(input())

brackets_counter = 0

for element in range(number_of_lines):
    element = input()
    if "(" in element or ")" in element:
        brackets_counter += 1

if brackets_counter % 2 == 0:
    print("BALANCED")
else:
    print("UNBALANCED")