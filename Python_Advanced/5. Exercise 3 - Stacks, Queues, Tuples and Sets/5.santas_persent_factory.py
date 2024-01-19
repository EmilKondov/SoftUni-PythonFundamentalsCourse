from collections import deque
# Getting the input from the console and entering basic data
materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

presents = {
150: "Doll",
250: "Wooden train",
300: "Teddy bear",
400: "Bicycle"
}
crafted = []
# Body 
while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    total_magic = current_magic * current_material

    if total_magic < 0:
        new_material_sum = current_magic + current_material
        materials.append(new_material_sum)
    elif total_magic not in presents and total_magic > 0:
        current_material += 15
        materials.append(current_material)
    elif total_magic == 0:
        if current_material == 0:
            magic.appendleft(current_magic)
        elif current_magic == 0:
            materials.append(current_material)
    else:

        if total_magic == 150:
            crafted.append(presents[150])
        elif total_magic == 250:
            crafted.append(presents[250])
        elif total_magic == 300:     
            crafted.append(presents[300])
        elif total_magic == 400:
            crafted.append(presents[400])


### Printing the result here
if ("Doll" in crafted and "Wooden train" in crafted) or ("Teddy bear" in crafted and "Bicycle" in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")


if magic:
    print("Magic left:", end=" ")
    print(*magic, sep=", ")
if materials:
    print("Materials left:", end=" ")
    print(*materials[::-1],sep=", ")

for toy in sorted(set(crafted)):
    print(f"{toy}:", end=" ")
    print(crafted.count(toy))



# 10 -5 20 15 -30 10
# 40 60 10 4 10

# 10 -5 20 15 -30 10
# 40 60 10 4 10 0

# 30 5 15 60 0 30
# -15 10 5 -15 25

# 30 10
# 15 10 5 0 10