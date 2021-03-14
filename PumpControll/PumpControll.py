

def pour(drink):
    for comp in drink.components:
        print(comp.name + " " + str(comp.amount * 200) + " ml")
