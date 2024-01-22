def rectangle(*args):
    lenght, width = args
    for el in args:
        if type(el) is not int or el <= 0:
            print("Enter a valid value!")
            exit()

    def area(lenght, width):
        return lenght * width

    def perimeter(lenght, width):
        return (lenght + width) * 2

    return f"""
Rectangle area: {area(lenght, width)}
Rectangle perimeter: {perimeter(lenght, width)}
"""

print(rectangle(2, 10))
#print(rectangle('2', 10))