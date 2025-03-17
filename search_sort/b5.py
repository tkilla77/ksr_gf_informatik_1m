def binary_search(l, v):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        elem = l[mid]
        if elem == v:
            return mid
        if v < elem:
            right = mid - 1
        else:
            left = mid + 1

def linear_search(l, v):
    for index, element in enumerate(l):
        if element == v:
            return index


def create_series(list, algo, count=10):
    increment = len(list) / count
    for index in range(0, len(list), increment):
        yield stop_watch(list, list[index], algo)

def stop_watch(list, value, algo):
    import time
    start = time.time()
    algo(list, value)
    return time.time() - start

from null79 import names, numbers

binary = list(create_series(names, binary_search))
linear = list(create_series(names, linear_search))

print(binary)
print(linear)