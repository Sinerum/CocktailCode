import json
from DataControll import Drink

CUP_SIZE = 200  # ml
drinks = []
bases = {}


def load_drinks(path):
    try:
        f = open(path).read()
    except:
        return "Invalid Path"
    data = json.loads(f)
    for x in data:
        create_drink(x, data[x])
    for x in drinks:
        print(x)
    print(bases)
    return True


def create_drink(name, comp):
    ingredients = []
    p = 0.0
    for y in comp:
        p += comp[y]
        if y.upper() not in bases.keys():
            return
        ingredients.append(Drink.Base(y.upper(), comp[y]))
    if p != 1:
        return name + " ingredients don't add up to 100%"
    else:
        drinks.append(Drink.Drink(name, ingredients))


def load_conf():
    try:
        f = open('../Gui/conf.json').read()
    except:
        return "Invalid Path"
    bases.update(json.loads(f))
