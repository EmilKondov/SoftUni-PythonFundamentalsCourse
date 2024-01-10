# text = list(input())
# stack = []
#
# for i in range(len(text)):
#     stack.append(text.pop())
#
# print("".join(stack))
#


### Second most simple way ###

text = list(input())

while text:
    print(text.pop(), end= "")
