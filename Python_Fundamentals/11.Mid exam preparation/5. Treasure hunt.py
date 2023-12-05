def loot(loot_items, first_item, second_item, third_item):
    for item in loot_items:
        if first_item != item:
            loot_items.insert(loot_items.index([0]), first_item)
        elif second_item != item:
            loot_items.insert(second_item, loot_items[0])
        elif third_item != item:
            loot_items.insert(third_item, loot_items[0])
    return loot_items

def drop(loot_items, index):
    pass

def steal(loot_items, count):
    pass

loot_items = input().split("|")
command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        item1, item2, item3 = command[1], command[2], command[3]
        loot_items = loot(loot_items, item1, item2, item3)
    elif action == "Drop":
        index = command[1]
        loot_items = drop(loot_items, index)
    elif action == "Steal":
        count = command[1]
        loot_items = steal(loot_items, count)
    command = input()