import numpy as np
from matplotlib import pyplot as plt
from typing import Union
from matplotlib.widgets import Slider

from lab3_2 import lagrange


def f(x: Union[int, float, np.ndarray]) -> float:
    return 1 / (1 + 25 * x ** 2)


def update(val):
    n=nodes_slider.val
    # noinspection PyTypeChecker
    given_points_x=list((x for x in np.arange(-5,5,10/(n))))
    #given_points_x[-1]=5
    given_points_y = list(f(x) for x in given_points_x)
    global x
    lagrange_plt.set_ydata(lagrange(x,given_points_x,given_points_y))
    given_points_x.append(5)
    given_points_y.append(f(5))
    points_plot.set_xdata(given_points_x)
    points_plot.set_ydata(given_points_y)
    fig.canvas.draw_idle()


if __name__ == '__main__':
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.25)
    x = np.linspace(-5, 5, 1000)

    """Plotting lagrange poly"""
    given_points_x = tuple(x for x in range(-5, 6))
    given_points_y = tuple(f(x) for x in given_points_x)
    lagrange_plt, = ax.plot(x, lagrange(x, given_points_x, given_points_y))

    """Plotting given points"""
    points_plot,=ax.plot(given_points_x, given_points_y, 'mo')

    """Calculating the difference"""
    print(f"{f(4.5)=}\n"
          f"lagrange_poly(4.5) = {lagrange(4.5, given_points_x, given_points_y)}\n"
          f"delta = {abs(f(4.5) - lagrange(4.5, given_points_x, given_points_y))}")

    """Plotting f(x)"""
    ax.plot(x, f(x), 'r')

    nodes_slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03])
    nodes_slider = Slider(nodes_slider_ax, 'Number of nodes', 10, 100, valinit=10, valstep=1)
    nodes_slider.on_changed(update)

    ax.grid()
    plt.show()
