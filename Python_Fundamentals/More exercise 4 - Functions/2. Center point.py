import math

x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

x = 0
y = 0
if abs(x1) <= abs(x2):
    x = x1
else:
    x = x2

if abs(y1) <= abs(y2):
    y = y1
else:
    y = y2

print(f"({math.floor(x)}, {math.floor(y)})")


