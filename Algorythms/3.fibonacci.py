# # First try usin if/els
# n = abs(int(input()))
# fibonacci = []
# for i in range(n):
#
#     if i == 0:
#         fibonacci.append(i)
#         a = 0
#         b = 1
#         c = a + b
#         a = b
#         b = c
#         fibonacci.append(b)
#         fibonacci.append(c)
#     else:
#         c = a + b
#         fibonacci.append(c)
#         a = b
#         b = c
# print(fibonacci)
# print(sum(fibonacci))

# #Second way - for loop
# l = [0, 1]
# def fibonacci(n):
#     n = abs(n)
#
#     if n < len(l):
#         return l[n]
#     else:
#         for i in range(len(l), n + 1):
#             sum = l[i - 1] + l[i - 2]
#             l.append(sum)
#         return l[n]
#
# n = int(input())
# for i in range(n):
#     print(f"fibonacci ( {i} ) = {fibonacci(i)}")
#     print((f"l = {l}"))


#Third way - recursion
def fibonacci(n):
    n = abs(n)

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)

n = int(input())
for i in range(n):
    print(f"fibonacci ( {i} ) = {fibonacci(i)}")