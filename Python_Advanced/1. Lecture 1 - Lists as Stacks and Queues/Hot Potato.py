from collections import deque

children = deque(input().split())
n_toss = int(input()) - 1

while len(children) > 1:
    children.rotate(-n_toss)
    removed_kid = children.popleft()
    print(f"Removed {removed_kid}")
print(f"Last is {children[0]}")

