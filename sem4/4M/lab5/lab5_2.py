from lab5_1 import simpson
from numpy import linspace
from math import pi as real_pi


x = (0, 0.5, 1)
y = tuple(1 / (1 + i ** 2) for i in x)
last_pi = simpson(x, y) * 4
while True:
    x = tuple(linspace(0, 1, len(x) + 2))
    y = tuple(1 / (1 + i ** 2) for i in x)
    pi = simpson(x, y) * 4
    if abs(pi - last_pi) < 10 ** (-6):
        break
    last_pi = pi
print(f'Number segments: {len(x) - 1}\n{pi=}\ndifference with true pi = {abs(real_pi - pi)}')
