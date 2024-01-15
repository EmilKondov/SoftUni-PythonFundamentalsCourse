count_of_lines = int(input())
elements_list = []

for _ in range(count_of_lines):
    elements = input().split()
    elements_list.extend(elements)

for element in set(elements_list):
    print(element)
