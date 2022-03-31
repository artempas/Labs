import numpy as np
from matplotlib.widgets import Slider

from lab3_2 import lagrange
from lab3_4 import f
from matplotlib import pyplot as plt
from numpy import pi, cos
from typing import Union


def update(val):
    n=nodes_slider.val
    given_points_x=chebyshev_nodes(-5,5,int(n))
    given_points_y = tuple(f(x) for x in given_points_x)
    global x
    lagrange_plt.set_ydata(lagrange(x,given_points_x,given_points_y))

    points_plot.set_xdata(given_points_x)
    points_plot.set_ydata(given_points_y)
    fig.canvas.draw_idle()
    ax.relim()
    ax.autoscale_view()


def chebyshev_nodes(a: Union[int, float], b: Union[int, float], n: int) -> tuple:
    return tuple((0.5 * (a + b) + 0.5 * (b - a) * cos((2 * k - 1)*pi / (2 * n))) for k in range(n + 1))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.set_autoscaley_on(True)
    fig.subplots_adjust(bottom=0.25)
    x = np.linspace(-5, 5, 1000)

    """Plotting lagrange poly"""
    given_points_x=chebyshev_nodes(-5,5,10)
    given_points_y = tuple(f(x) for x in given_points_x)
    lagrange_plt, = ax.plot(x, lagrange(x, given_points_x, given_points_y),lw=4)

    """Plotting given points"""
    points_plot, = ax.plot(given_points_x, given_points_y, 'mo')


    """Plotting f(x)"""
    ax.plot(x, f(x), 'r')

    nodes_slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03])
    nodes_slider = Slider(nodes_slider_ax, 'Number of nodes', 10, 100, valinit=10, valstep=1)
    nodes_slider.on_changed(update)

    ax.grid()
    plt.show()