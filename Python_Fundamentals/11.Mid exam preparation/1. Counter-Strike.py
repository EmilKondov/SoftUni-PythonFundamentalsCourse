############## My initial solution ###################
initial_energy = int(input())
command = input()
battles_won = 0
flag = True

while command != 'End of battle':
    needed_energy = int(command)
    if needed_energy <= initial_energy and initial_energy >0:
        battles_won += 1
        initial_energy -= needed_energy

        if battles_won % 3 == 0:
            initial_energy += battles_won
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        flag = False
        break
    command = input()

if flag:
    print(f"Won battles: {battles_won}. Energy left: {initial_energy}")





############ More simple solution ###################

energy = int(input())
distance = input()

battles_won = 0

while distance != "End of battle":
    distance = int(distance)

    if energy >= distance and energy > 0:
        energy -= distance
        battles_won += 1

        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy ")
        break

    distance = input()
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")