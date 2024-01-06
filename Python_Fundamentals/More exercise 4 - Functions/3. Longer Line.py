from math import floor, hypot

x1 = float(input())
y1 = float(input())
a = hypot(x1, y1)

x2 = float(input())
y2 = float(input())
b = hypot(x2, y2)

x3 = float(input())
y3 = float(input())
c = hypot(x3, y3)

x4 = float(input())
y4 = float(input())
d = hypot(x4, y4)

def one_point(a, c):
    if a > c:
        point_of_line = x1, y1
        return a
    else:
        point_of_line = x3, y3
        return c

def second_point(b, d):
    if b > d:
        second_point_of_line = x2, y2
        return b
    else:
        second_point_of_line = x4, y4
        return d


one_point_of_the_line = one_point(a, c)
second_point_of_the_line = second_point(b, d)

X1 = 0
Y1 = 0

X2 = 0
Y2 = 0

if abs(one_point_of_the_line) < abs(second_point_of_the_line):
    if one_point_of_the_line == a:
        X1 = x1
        Y1 = y1
    elif one_point_of_the_line == c:
        X1 = x3
        Y1 = y3

    if second_point_of_the_line == d:
        X2 = x4
        Y2 = y4
    elif second_point_of_the_line == b:
        X2 = x2
        Y2 = y2

else:
    if one_point_of_the_line == a:
        X2 = x1
        Y2 = y1
    elif one_point_of_the_line == c:
        X2 = x3
        Y2 = y3

    if second_point_of_the_line == d:
        X1 = x4
        Y1 = y4
    elif second_point_of_the_line == b:
        X1 = x2
        Y1 = y2


print(f"({X1:.0f}, {Y1:.0f})({X2:.0f}, {Y2:.0f})")




# You will be given the coordinates of four points. The first and the second pair of points form two different lines.
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point
# which is closer to the center of the coordinate system (0, 0). You can reuse the method that you wrote for the
# previous problem. If the lines are of equal length, print only the first one. The resulting coordinates must be
# formatted to the lower integer.

#1. First find out which pair of point will form a longer line
#2. Once you know the point of the longer line use the script from your previous task to find out which is closer to the center.
#3. The one that is closer should be used as a starting point of the line
