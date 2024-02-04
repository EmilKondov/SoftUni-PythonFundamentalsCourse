from collections import deque

#input
elves_energy = deque([int(x) for x in input().split()])   # deque
material_boxes = [int(y) for y in input().split()] # stack

total_energy_used = 0
total_toys_made = 0
turn = 0

#logic
while elves_energy and material_boxes:
    current_elf = elves_energy.popleft()
    current_box = material_boxes[-1]

    if current_elf < 5:
        continue

    turn += 1
    current_toys_made = 0

    if turn % 3 == 0:
        current_box *= 2
        current_toys_made += 1

    if current_elf >= current_box:
        total_energy_used += current_box
        current_elf -= current_box

        if turn % 5 != 0:
            current_elf += 1
            current_toys_made += 1
        else:
            current_toys_made = 0

        material_boxes.pop()

    else:
        current_elf *= 2
        current_toys_made = 0

    total_toys_made += current_toys_made
    elves_energy.append(current_elf)

#output
print(f"Toys: {total_toys_made}")
print(f"Energy: {total_energy_used}")

if elves_energy:
    print(f"Elves left: {', '.join(str(x) for x in elves_energy)}")
if material_boxes:
    print(f"Boxes left: {', '.join(str(y) for y in material_boxes)}")
