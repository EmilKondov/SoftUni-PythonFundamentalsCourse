initial_energy = int(input())
command = input()
battles_won = 0
flag = True

while command != 'End of battle':
    needed_energy = int(command)
    if battles_won % 3 == 0:
        initial_energy += battles_won
    if needed_energy <= initial_energy:
        battles_won += 1
        initial_energy -= needed_energy
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        flag = False
        break
    command = input()

if flag:
    print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
else:
    pass
