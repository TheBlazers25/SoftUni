def rectangle(length, width):
    if not isinstance(length, int) or length < 0 or width < 0:
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


