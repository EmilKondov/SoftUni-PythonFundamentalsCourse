def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter a valid value!"

    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
print(rectangle(2, 10))
