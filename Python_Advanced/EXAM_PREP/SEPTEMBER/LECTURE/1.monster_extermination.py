from collections import deque

armour_values = deque(map(int, input().split(",")))
striking_impact = [int(x) for x in input().split(",")]

monsters_killed = 0
while armour_values and striking_impact:
    armour = armour_values.popleft()
    impact = striking_impact.pop()

    if impact >= armour:
        monsters_killed += 1
        impact -= armour
        if striking_impact:
            striking_impact[-1] += impact
        elif not striking_impact and impact > 0:
            striking_impact.append(impact)
    else:
        armour_values.append(armour - impact)


if not armour_values:
    print("All monsters have been killed!")
if not striking_impact:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")
