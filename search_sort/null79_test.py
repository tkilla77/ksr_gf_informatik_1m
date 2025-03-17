from null79 import names, numbers
import time

def linear_search(li, el):
    for i in range(len(li)):
        if li[i] == el:
            return i
    return None

def stopwatch(name):
    start = time.time()
    index = linear_search(names, name)
    elapsed = time.time() - start
    print("Lineare Suche für {0} dauerte {1:.1f}s".format(name, elapsed))

stopwatch('Alaska')
stopwatch('Annina')
print(names[linear_search(numbers, '0791234567')])

name = 'Lyanna'


linear_search(names, name)