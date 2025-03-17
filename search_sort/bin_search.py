from null79 import names, numbers
import time

def binary_search(l, v):
    left = 0
    right = len(l) - 1
    
    while left <= right:
        middle = (left + right) // 2
        element = l[middle]
        if element == v:
            return middle  # Gefunden!
        if v < element:
            # Links weitersuchen
            right = middle - 1
        else:
            # Rechts weitersuchen
            left = middle + 1
            
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
#stopwatch(linear_search, 'Lyanna')
stopwatch(binary_search, 'Operla')