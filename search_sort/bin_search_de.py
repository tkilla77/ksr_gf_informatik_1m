from null79 import names, numbers
import time

def binary_search(names, name):
    links = 0
    rechts = len(names) - 1
    
    while links <= rechts:
        mitte = (links + rechts) // 2
        if names[mitte] == name:
            return mitte  # Gefunden!
        if name < names[mitte]:
            rechts = mitte - 1
        else:
            links = mitte + 1
            
    return None  # Nichts gefunden

def linear_search(li, el):
    for i in range(len(li)):
        if li[i] == el:
            return i
    return None

def stopwatch(algo, name):
    start = time.time()
    index = algo(names, name)
    telnr = numbers[index]
    elapsed = time.time() - start
    print('Die Nummer von {0} lautet {1}! Die Suche dauerte {2:.2f}s.'.format(name, telnr, elapsed))

stopwatch(linear_search, 'Annina')
stopwatch(binary_search, 'Annina')
stopwatch(linear_search, 'Lyanna')
stopwatch(binary_search, 'Lyanna')