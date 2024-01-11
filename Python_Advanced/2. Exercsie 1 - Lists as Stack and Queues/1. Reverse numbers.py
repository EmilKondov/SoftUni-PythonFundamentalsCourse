given_int = list(input())
stack = []

while given_int:
    stack.append(given_int.pop())
print("".join(stack))
