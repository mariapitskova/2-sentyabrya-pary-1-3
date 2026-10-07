class Graph:
    def __init__(self, data):
        self.data = data
        self.is_show = True

    def show_table(self):
        if self.is_show:
            print(" ".join(str(x) for x in self.data))
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show

g = Graph([1, 2, 3, 4, 5])

g.show_table()
g.set_show(False)
g.show_table()
g.set_show(True)
g.show_table()         