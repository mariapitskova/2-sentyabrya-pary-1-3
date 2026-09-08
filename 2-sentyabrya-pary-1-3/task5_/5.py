class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

fig = Figure((30, 40), 2, "черный")
print(fig.coords, fig.width, fig.color)