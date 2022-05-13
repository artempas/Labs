from typing import Union, Callable

import matplotlib.pyplot as plt
import numpy as np
from numpy import log

np.seterr(all='raise')


def diff(f: Callable, x: Union[int, float], accuracy: Union[int, float]):
    h = 1
    diff_val = (f(x + h) - f(x)) / h
    next_diff_val = (f(x + h/2) - f(x)) / (h/2)
    while abs(next_diff_val-diff_val)>accuracy:
        h=h/2
        diff_val=next_diff_val
        next_diff_val=(f(x + h/2) - f(x)) / (h/2)


    return diff_val


fig, ax = plt.subplots()
f = log
print(diff(f, 2, 10**(-6)))
x = np.linspace(0.00000001, 4, 1000)
y = f(x)
y_diff = list(diff(f, i, 0.001) for i in x)
plt.plot(x, y, 'b', label='ln(x)')
plt.plot(x, y_diff, 'r',label="ln(x)'")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.ylim([-25,25])
plt.legend()
plt.grid()
plt.show()
