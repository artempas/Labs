from typing import Union

import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, pi

GIVEN_POINTS_X = (0, 0.25, 0.5, 0.75, 1)
GIVEN_POINTS_Y = (0, sin(0.25 * pi), sin(pi / 2), sin(0.75 * pi), sin(pi))
POINTS_TO_DEFINE = (0, 1 / 6, 1 / 3, 1 / 2)


def lagrange(var: Union[int, float, np.ndarray], x_i: tuple, y_i: tuple) -> float:
    assert len(x_i) == len(y_i)
    phi = []
    for x in x_i:
        numerator = 1
        denominator = 1
        for i in x_i:
            if not i == x:
                numerator *= (var - i)
                denominator *= (x - i)
        phi.append(numerator / denominator)
    return sum(y_i[i] * phi[i] for i in range(len(x_i)))


if __name__ == '__main__':
    x = np.linspace(0, 1)
    fig, ax = plt.subplots()
    plt.plot(x, sin(pi * x), 'b', linewidth=4)
    plt.plot(GIVEN_POINTS_X, GIVEN_POINTS_Y, 'go')
    plt.plot(x, lagrange(x, GIVEN_POINTS_X, GIVEN_POINTS_Y), 'r')
    plt.grid()
    plt.show()
