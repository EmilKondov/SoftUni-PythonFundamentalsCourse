from collections import deque

stack_of_clothes = deque(input().split())
rack_capacity = int(input())
current_rack_capacity = rack_capacity
racks_counter = 0
clothes_sum = 0

while stack_of_clothes:
    if clothes_sum >= rack_capacity or current_rack_capacity < int(stack_of_clothes[-1]):
        racks_counter += 1
        current_rack_capacity = rack_capacity
        clothes_sum = 0
    else:
        piece_of_cloth = stack_of_clothes.pop()
        clothes_sum += int(piece_of_cloth)
        current_rack_capacity -= int(piece_of_cloth)
else:
    racks_counter += 1
print(racks_counter)
