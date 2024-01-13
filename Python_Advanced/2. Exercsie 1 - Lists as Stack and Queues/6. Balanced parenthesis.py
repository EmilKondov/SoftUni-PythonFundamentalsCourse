# from collections import deque
#
# parenthesis = deque(input())
#
# open_parenthesis = deque()
#
# while parenthesis:
#     current_parenthesis = parenthesis.popleft()
#
#     if current_parenthesis in "{[(":
#         open_parenthesis.append(current_parenthesis)
#     elif not open_parenthesis:
#         print("NO")
#         break
#     else:
#         if f"{open_parenthesis.pop() + current_parenthesis}" not in "(){}[]":
#             print("NO")
#             break
# else:
#     print("YES")

### Second solution ###

parenthesis = input()
stack = []

opening = {'{': '}', '[': ']', '(': ')'}

for char in parenthesis:
    if char in opening:   # checks if char is in any of the opening dictionary keys
        stack.append(char)
    elif char in opening.values(): # check if char in any of the values of the dictionary
        if not stack or opening[stack.pop()] != char:
            print("NO")
            break
else:
    print("YES")