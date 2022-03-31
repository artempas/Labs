import time
from random import randint



def binary_search(el: int, mas: list):
    low = 0
    high = len(mas) - 1
    if el < mas[0]:
        return low
    if el > mas[-1]:
        return high + 1
    while high != low:
        mid = low + (high - low) // 2
        if el >= mas[mid]:
            low = mid
        if el <= mas[mid + 1]:
            high = mid

    return low + 1

for n in (10,0):
    n=10
    mas = [randint(-5000, 5000) for i in range(n)]
    print(mas)
    start=time.time()
    sorted_mas = []
    if mas[0] >= mas[1]:
        sorted_mas = [mas.pop(1), mas.pop(0)]
    else:
        sorted_mas = [mas.pop(0), mas.pop(0)]

    for _ in range(len(mas)):
        # print(f'{sorted_mas=}\nTrying to insert {mas[0]}\n{i=}\n')
        ind = binary_search(mas[0], sorted_mas)
        sorted_mas.insert(ind, mas.pop(0))

    print(sorted_mas)

    sorted = True
    last = sorted_mas[0]
    for i in sorted_mas:
        if i >= last:
            last = i
        else:
            sorted = False
            break
    print(f'{sorted=}')
    print('\033[92m'+f"{n=}, time taken {(time.time()-start)*10**6}"+'\033[0m')

'''https://www.geogebra.org/graphing/uq748umy'''