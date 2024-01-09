from collections import deque
water_qty = int(input())
queue = deque()
name = input()
#add people to queue
while name != "Start":
    queue.append(name)
    name = input()
command = input()
while command != "End":
    if "refill" in command:
        action, litres = command.split()
        water_qty += int(litres)
    else:
        litres = int(command)
        if litres <= water_qty:
            water_qty -= litres
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    command = input()
print(f"{water_qty} liters left")
