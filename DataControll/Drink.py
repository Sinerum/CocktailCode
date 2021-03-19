from DataControll import PumpControll


class Drink:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def __str__(self):
        x = self.name + ": ("
        for y in self.components:
            x += " " + str(y)
        return x + ")"

    def pour(self):
        PumpControll.pour(self)


class Base:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return self.name + ":" + str(self.amount)

