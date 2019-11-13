import json
from DataControll import Drink

drinks = []


def load_drinks(path):
    try:
        f = open(path).read()
    except:
        return "Invalid Path"
    data = json.loads(f)
    for x in data:
        c = []
        for y in data[x]:
            c.append(Drink.Base(y, data[x][y]))
        drinks.append(Drink.Drink(x, c))
    for x in drinks:
        print(x)
    return drinks


def get_drinks_str():
    out = ""
    for x in drinks:
        out += str(x)
    return out
