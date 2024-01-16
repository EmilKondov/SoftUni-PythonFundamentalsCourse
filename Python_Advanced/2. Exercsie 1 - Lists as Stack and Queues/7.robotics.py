from collections import deque
from datetime import datetime, timedelta
robots = {}  # robot_name: [processing_time, time_till_free]

robots_list = [x for x in input().split(";")]
for _ in robots_list:
    robot_name, value = _.split("-")
    robots[robot_name] = [int(value), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
production_line = deque()


while True:
    product = input()

    if product == "End":
        break

    production_line.append(product)


while production_line:
    factory_time += timedelta(0, 1)
    product = production_line.popleft()

    free_robots = []

    for robot_name, value in robots.items():
        if value[1] != 0:
            robots[robot_name][1] -= 1
        if value[1] == 0:
            free_robots.append([robot_name, value])


    if not free_robots:
        production_line.append(product)
        continue

    robot_name, value = free_robots[0] # ronbots_name = "Rob", data = [15, 0]
    robots[robot_name][1] = value[0] # {"Rob": [15, 15]}
    print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")
