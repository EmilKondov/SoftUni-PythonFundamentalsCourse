import math

def long_line(a, b , c, d):
    if a > c:

    else:

    if b > d:
        pass
    else:



x1 = float(input())
y1 = float(input())
a = abs(x1) + abs(y1)

x2 = float(input())
y2 = float(input())
b = abs(x2) + abs(y2)

x3 = float(input())
y3 = float(input())
c = abs(x3) + abs(y3)

x4 = float(input())
y4 = float(input())
d = abs(x4) + abs(y4)


if a > c:
    point_of_line = x1, y1
else:
    point_of_line = x3, y3

if b > d:
    second_point_of_line = x2, y2
else:
    second_point_of_line = x4, y4

x = 0
y = 0

if abs(x1) <= abs(x2) or \
        abs(x1) <= abs(x2) or \
        abs(x1) <= abs(x3) or \
        abs(x1) <= abs(x4):
    x = x1
elif abs(x2) <= abs(x3) or \
        abs(x2) <= abs(x4):
    x = x2
elif abs(x3) <= abs(x4):
    x = x3
else:
    x = x2

if abs(y1) <= abs(y2) or \
        abs(y1) <= abs(y2) or \
        abs(y1) <= abs(y3) or \
        abs(y1) <= abs(y4):
    y = y1
elif abs(y2) <= abs(y3) or \
        abs(y2) <= abs(y4):
    y = y2
elif abs(y3) <= abs(y4):
    y = y3
else:
    y = y2

longer_line = long_line(a, b, c, d)
print(f"({math.floor(x)}, {math.floor(y)})")


# You will be given the coordinates of four points. The first and the second pair of points form two different lines.
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point
# which is closer to the center of the coordinate system (0, 0). You can reuse the method that you wrote for the
# previous problem. If the lines are of equal length, print only the first one. The resulting coordinates must be
# formatted to the lower integer.

#1. First find out which pair of point will form a longer line
#2. Once you know the point of the longer line use the script from your previous task to find out which is closer to the center.
#3. The one that is closer should be used as a starting point of the line