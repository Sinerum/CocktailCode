import time

from DataControll import Data


def pour(drink):
    scheduel = {}
    for comp in drink.components:
        pump = Data.bases[comp.name]
        if pump < 0:
            return
        scheduel[pump] = comp.amount*Data.CUPSIZE

    for pump in scheduel.keys():
        # start pump

        print(pump, ' ', time.time())
    start_time = time.time()
    print(start_time)
    while bool(scheduel):
        for s in scheduel.items():
            if (s[1]) < (time.time() - start_time)*1000:
                scheduel.pop(s[0])

                # stop pump
                print(s[0], ' ' , time.time())
                break

