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
        p = 0.0
        for y in data[x]:
            p += data[x][y]
            c.append(Drink.Base(y, data[x][y]))
        if p != 1:
            return x + " ingredients dont add up to 100%"
        else:
            drinks.append(Drink.Drink(x, c))
    for x in drinks:
        print(x)
    return True


def get_drinks_str():
    out = ""
    for x in drinks:
        out += str(x)
    return out
