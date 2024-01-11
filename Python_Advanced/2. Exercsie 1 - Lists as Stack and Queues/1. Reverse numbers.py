from collections import deque
# given_int = deque(input().split())
#
# for _ in range(len(given_int)):
#     print(given_int.pop(), end=" ")
#

numbers = deque(input().split())

numbers.reverse()

print(*numbers)