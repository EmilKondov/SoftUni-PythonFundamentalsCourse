def loot(loots, list_items):
    for item in list_items:
        if item not in loots:
            loots.insert(0, item)
    return loots

def drop(loots, target_index):
    if target_index in range(len(loots)):
        removed_loot = loots.pop(target_index)
        loots.append(removed_loot)
    return loots

def steal(loots, count_of_steal):
    if count_of_steal >= len(loots):
        print(",".join(loots))
        loots = []
    else:
        steal_index = len(loots) - count_of_steal
        print(", ".join(loots[steal_index:]))
        loots = loots[0:steal_index]
    return loots

loot_items = input().split("|")
command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        items = command[1:]
        loot_items = loot(loot_items, items)
    elif action == "Drop":
        index = int(command[1])
        loot_items = drop(loot_items, index)
    elif action == "Steal":
        count = int(command[1])
        loot_items = steal(loot_items, count)
    command = input()

if not loot_items:
    print(f"Failed treasure hunt.")
else:
    average_gain = sum(len(item) for item in loot_items) / len(loot_items)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
