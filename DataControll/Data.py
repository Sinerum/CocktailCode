import json
from DataControll import Drink


def load_drinks(path):
    f = open(path).read()
    data = json.loads(f)
    drinks = []
    for x in data:
        c = []
        for y in data[x]:
            c.append(Drink.Base(y, data[x][y]))
        drinks.append(Drink.Drink(x, c))
    for x in drinks:
        print(x)


load_drinks(input())