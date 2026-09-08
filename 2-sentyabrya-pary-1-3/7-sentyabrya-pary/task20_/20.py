class Cart:
    def __init__(self):
        self.goods = []  # Список товаров

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        if 0 <= indx < len(self.goods):
            del self.goods[indx]

    def get_list(self):
        return [f"{item.name}: {item.price}" for item in self.goods]

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()

cart.add(TV("Samsung Neo QLED 8K", 250000))
cart.add(TV("LG G3 OLED evo", 180000))
cart.add(Table("Дубовый обеденный стол", 15000))
cart.add(Notebook("Apple MacBook Pro 16", 320000))
cart.add(Notebook("ASUS ROG Zephyrus G16", 210000))
cart.add(Cup("Керамическая кружка с подогревом", 1500))

for item in cart.get_list():
    print(item)


