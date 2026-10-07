class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")


class Line(Figure):
    def draw(self):
        print("Рисуется линия")


class Rect(Figure):
    def draw(self):
        print("Рисуется прямоугольник")


class Ellipse(Figure):
    def draw(self):
        print("Рисуется эллипс")

class Triangle(Figure):
    def draw(self):
        print("Рисуется треугольник")


figures = [
    Line([(0, 0), (10, 10)], 2, "red"),
    Rect([(0, 0), (5, 5)], 1, "blue"),
    Ellipse([(0, 0), (8, 4)], 1, "green"),
]

print("До добавления Triangle:")
for fig in figures:
    fig.draw()

figures.append(Triangle([(0, 0), (5, 0), (2, 4)], 1, "black"))

print("\nПосле добавления Triangle:")
for fig in figures:
    fig.draw()