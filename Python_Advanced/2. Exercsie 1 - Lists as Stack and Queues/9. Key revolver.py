from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = [int(x) for x in input().split()]
locks = deque([int(y) for y in input().split()])
intelligence_value = int(input())

current_gun_barrel = barrel_size
bullet_counter = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks[0]

    if bullet <= lock:
        lock = locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    bullet_counter += 1
    current_gun_barrel -= 1

    if current_gun_barrel == 0 and bullets:
        current_gun_barrel = barrel_size
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence_value - (bullet_counter * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
