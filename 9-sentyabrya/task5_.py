class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color

p1 = Point(10, 20)          # без цвета → black
p2 = Point(12, 5, "red")    # с цветом
p3 = Point(7, 8, "green")   # ещё одна с цветом

points = [p1, p2, p3]

for p in points:
    print(f"Point({p.x}, {p.y}, '{p.color}')")