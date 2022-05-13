from typing import Callable, Union
from numbers import Real, Rational
from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np
from numpy import log


def diff_h(f: Callable, x: Real, h: float):
    return (f(x + h) - f(x)) / h


def diff_2h(f: Callable, x: Real, h: float) -> float:
    return (f(x + h) - f(x - h)) / (2 * h)


def delta(f: Callable, x: Real, h: float, diff_to_delta:Callable) -> float:
    return abs(diff_to_delta(f, x, h) - diff_to_delta(f, x, h / 2))


print("Delta h")
last_delta = delta(log, 2, 1, diff_h)
for h in (1 / 2, 1 / 4, 1 / 8):
    print(f"  {h=},\t\tdelta={delta(log, 2, h, diff_h)},\t\trelative delta={last_delta / delta(log, 2, h, diff_h)}")
    last_delta = delta(log, 2, h, diff_h)

print("Delta 2h")
last_delta = delta(log, 2, 1, diff_2h)
for h in (1 / 2, 1 / 4, 1 / 8):
    print(f"  {h=},\t\tdelta={delta(log, 2, h, diff_2h)},  \trelative delta={last_delta / delta(log, 2, h, diff_2h)}")
    last_delta = delta(log, 2, h, diff_2h)

h=np.linspace(1/2048,1,11)
delta_h_y=list(delta(log, 2, h_i, diff_h) for h_i in h)
delta_2h_y=list(delta(log,2,h_i, diff_2h) for h_i in h)
fig,ax=plt.subplots()
plt.plot(h,delta_h_y,'bo',label="delta_h")
plt.plot(h,delta_2h_y,'ro',label="delta_2h")
plt.axvline(0,color='black')
plt.axhline(0,color='black')
plt.grid()
plt.xlabel('h')
plt.ylabel('delta')
plt.legend()
plt.show()


