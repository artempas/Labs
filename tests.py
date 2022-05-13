import math
import numpy as np
from matplotlib import pyplot as plt

def simpson(f, a, b, n):
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, n // 2 + 1):
        k += 4 * f(x)
        x += 2 * h

    x = a + 2 * h
    for i in range(1, n // 2):
        k += 2 * f(x)
        x += 2 * h
    return (h / 3) * (f(a) + f(b) + k)


def trap(f, a, b, n):
    h = (b - a) / n
    s = (f(a) + f(b)) / 2
    x = a + h
    while (x <= b - h):
        s += f(x)
        x += h
    return h * s

def task2():
    f4 = lambda x: 1 / (1 + x ** 2)

    print("pi =", str(4 * simpson(f4, 0, 1, 6)))

    x4 = [i for i in range(2, 10, 2)]
    razn4 = [math.log2(abs(math.pi - 4 * simpson(f4, 0, 1, i))) for i in x4]

    plt.plot(x4, razn4, 'ro')
    plt.show()

task2()