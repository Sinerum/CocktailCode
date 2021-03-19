import time

from DataControll import Data


def pour(drink):
    schedule = {}
    for comp in drink.components:
        pump = Data.bases[comp.name]
        if pump < 0:
            return
        schedule[pump] = comp.amount*Data.CUP_SIZE

    for pump in schedule.keys():
        # start pump

        print(pump, ' ', time.time())
    start_time = time.time()
    print(start_time)
    while bool(schedule):
        for s in schedule.items():
            if (s[1]) < (time.time() - start_time)*1000:
                schedule.pop(s[0])

                # stop pump
                print(s[0], ' ' , time.time())
                break

