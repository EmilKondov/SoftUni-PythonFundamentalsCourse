#from collections import deque
#
# food_quantity = int(input())
# orders = deque(input().split())
#
# print(max(int(x) for x in orders))
#
# while orders:
#     if food_quantity >= int(orders[0]):
#         order = orders.popleft()
#         food_quantity -= int(order)
#     else:
#         print(f"Orders left:", *orders)
#         break
# else:
#     print("Orders complete")

### Second solution ### 

from collections import deque
food = int(input())
orders = deque(input().split())

print(max(int(x) for x in orders))

for order in orders.copy():
    if food >= int(order):
        order = orders.popleft()
        food -= int(order)
    else:
        print(f"Orders left:", *orders)
        break
else:
    print("Orders complete")