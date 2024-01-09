water_qty = int(input())
queue = []
command = input()

while command != "End":
    while command != "Start":
        queue.append(command)
        command = input()
    command = input()
    if command.isdigit():
        liters = int(command)
        if water_qty >= liters:
            water_qty -= liters
            queue.pop()
    elif command == "refill":
        refill_qty = command[1]
        water_qty += refill_qty
