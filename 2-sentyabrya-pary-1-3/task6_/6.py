class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

line = Line((0, 0), 4, "черный", 10)
rect = Rect((1, 1), 7, "розовый", 5)
ellipse = Ellipse((2, 2), 9, "голубой", 7)

print(f"Line: {line.coords}, {line.width}, {line.color}, {line.length}")
print(f"Rect: {rect.coords}, {rect.width}, {rect.color}, {rect.height}")
print(f"Ellipse: {ellipse.coords}, {ellipse.width}, {ellipse.color}, {ellipse.radius}")