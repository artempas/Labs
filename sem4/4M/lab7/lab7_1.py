from typing import Union
from numpy import linspace
import matplotlib.pyplot as plt


def euler(f: callable, start_point: tuple[Union[int, float], Union[int, float]], end: Union[int, float], n: int = 50) \
        -> tuple[tuple[float], list[float]]:
    """
    :param f: Function to solve f(x,y)
    :param start_point: Tuple of (x,y) as initial condition
    :param end: end x
    :param n: number of points
    :return: (X:tuple,Y:tuple)
    """
    h = abs(start_point[0] - end) / n
    x = tuple(start_point[0] + i * h for i in range(n))
    y = [start_point[1]]
    for i in range(1, len(x)):
        y.append(y[i - 1] + h * f(x[i - 1], y[i - 1]))
    return x, y


if __name__ == '__main__':
    f = lambda x, y: x ** 2
    ex, ey = euler(f, (0, 1), 5, 100)
    x = linspace(0, 5)
    y = tuple(i ** 3 / 3 + 1 for i in x)
    diff = max(abs(ey[i] - (ex[i] ** 3 / 3 + 1)) for i in range(len(ex)))
    print(f'Max difference between euler and analytical is {diff}')
    plt.plot(ex, ey, 'r', label="euler's solution")
    plt.plot(x, y, 'b', label='Analytical solution')
    plt.axhline(color='k')
    plt.axvline(color='k')
    plt.legend()
    plt.grid()
    plt.show()
