# First try usin if/els
n = int(input())
fibonacci = []
for i in range(n):
    if i == 0:
        fibonacci.append(i)
        a = 0
        b = 1
        c = a + b
        a = b
        b = c
        fibonacci.append(b)
        fibonacci.append(c)
    else:
        c = a + b
        fibonacci.append(c)
        a = b
        b = c

print(fibonacci)
print(sum(fibonacci))