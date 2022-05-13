import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


def trapezoidal_rule(x_i, y_i):
    assert len(x_i) == len(y_i) and len(x_i) >= 2
    y = list(y_i)
    y[0] /= 2
    y[-1] /= 2
    h = x_i[1] - x_i[0]
    return (sum(y) * h)


def simpson(x_i, y_i):
    assert len(x_i) == len(y_i) and len(x_i) >= 2
    if len(x_i) % 2 != 1:
        raise ValueError('Length of the array must be even')
    h = (x_i[-1] - x_i[0]) / (len(x_i) - 1)
    return h / 3 * (y_i[0] + y_i[-1] + 2 * sum(y_i[i] for i in range(2, len(y_i) - 1) if i % 2 == 0) + 4 * sum(
        y_i[i] for i in range(len(y_i)) if i % 2 == 1))


def draw_dashed_xi(x, y):
    assert len(x) == len(y)
    for i in range(len(y)):
        ax.plot([x[i], x[i]], [0, y[i]], 'k--', linewidth=1)


def connect_xi(x, y):
    assert len(x) == len(y)
    for i in range(len(y) - 1):
        ax.plot([x[i], x[i + 1]], [y[i], y[i + 1]], 'r', linewidth=1)


def update(ax, val):
    ax.cla()
    x_i = list(np.linspace(0, 1, val + 1))
    y_i = tuple(i ** 3 for i in x_i)
    ax.plot(x, x ** 3, label='x^3')
    draw_dashed_xi(x_i, y_i)
    connect_xi(x_i, y_i)
    ax.set_xlabel(f"trapeziodal={trapezoidal_rule(x_i, y_i)}\nsimpson={simpson(x_i, y_i)}", fontsize='large',
                  fontweight='bold')
    ax.axvline(0, color='black')
    ax.axhline(0, color='black')
    ax.grid()
    ax.legend()


if __name__ == '__main__':
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    x = np.linspace(0, 1)
    x_i = tuple(np.linspace(0, 1, 11))
    y_i = tuple(i ** 3 for i in x_i)
    ax.plot(x, x ** 3, label='x^3')
    draw_dashed_xi(x_i, y_i)
    connect_xi(x_i, y_i)
    ax.set_xlabel(f"trapeziodal={trapezoidal_rule(x_i, y_i)}\nsimpson={simpson(x_i, y_i)}", fontsize='large',
                  fontweight='bold')
    ax.axvline(0, color='black')
    ax.axhline(0, color='black')
    ax.grid()
    nodes_slider_ax = fig.add_axes([0.25, 0.01, 0.65, 0.03])
    nodes_slider = Slider(nodes_slider_ax, 'Number of segments', 2, 100, valinit=10, valstep=2)
    nodes_slider.on_changed(lambda val: update(ax, val))
    ax.legend()
    plt.show()
