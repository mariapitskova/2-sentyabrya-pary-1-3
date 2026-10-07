class DataBase:
    lst_data = []
    FIELDS = ("id", "name", "old", "salary")

    def insert(self, data):
        for record in data:
            values = record.split()
            item = dict(zip(self.FIELDS, values))
            self.lst_data.append(item)

    def select(self, a, b):
        return self.lst_data[a:b + 1]

db = DataBase()
db.insert(["1 Сергей 35 120000", "2 Анна 28 90000", "3 Иван 42 150000"])

print("lst_data:", db.lst_data)
print("select(0, 1):", db.select(0, 1))