def rectangle(lenght: int, width: int):
    if type(lenght) != "int" or type(width) != "int":
        return f"Enter valid values!"

    def area(lenght, width):
        return lenght * width

    def perimeter(lenght, width):
        return (lenght + width) * 2

    return f"""
Rectangle area: {area(lenght, width)}
Rectangle perimeter: {perimeter(lenght, width)}
"""

print(rectangle(2, 10))