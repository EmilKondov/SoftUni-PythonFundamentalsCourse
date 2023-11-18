body_parts_lst = []

for current_part in range(3):
    current_part = input()
    body_parts_lst.append(current_part)

body_parts_lst[0], body_parts_lst[2] = body_parts_lst[2], body_parts_lst[0]
print(body_parts_lst)


