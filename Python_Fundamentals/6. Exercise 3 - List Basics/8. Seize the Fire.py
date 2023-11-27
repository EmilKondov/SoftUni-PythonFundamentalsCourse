cells = input().split("#")
amount_of_water = int(input())


total_effort = 0
total_fire = 0
cells_put_out_of_fire = []

for cell in cells:
    cell_list = cell.split(" = ")
    type_of_fire = str.lower(cell_list[0])
    range_of_fire = int(cell_list[1])
    cell_is_valid = False
    if type_of_fire == 'high':
        if 81 <= range_of_fire <= 125:
            cell_is_valid = True
    elif type_of_fire == 'medium':
        if 51 <= range_of_fire <= 80:
            cell_is_valid = True
    elif type_of_fire == 'low':
        if 1 <= range_of_fire <= 50:
            cell_is_valid = True
    if cell_is_valid:
        if amount_of_water >= range_of_fire:
            amount_of_water -= range_of_fire
            effort = range_of_fire * 0.25
            total_effort += effort
            total_fire += range_of_fire
            cells_put_out_of_fire.append(range_of_fire)
    cell_is_valid = False
print("Cells:")
for cell_put_out_of_fire in cells_put_out_of_fire:
    print(f" - {cell_put_out_of_fire}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
