import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, pi

t = [0, 1 / 6, 1 / 3, 1 / 2, 1]


def f(x):
    return sin(x * pi)


def linear_interpolation(t, y):
    t_i=[0,1/4,1/2,3/4,1]
    for i in range(len(t_i) - 1):
        x = np.linspace(t_i[i], t_i[i + 1])
        plt.plot(x, y(x[0]) + (y(x[-1]) - y(x[0])) / (x[-1] - x[0]) * (x - x[0]), 'g')
        for i in t:
            if x[0]<=i<x[-1]:
                plt.plot(i,y(x[0]) + (y(x[-1]) - y(x[0])) / (x[-1] - x[0]) * (i - x[0]),'go')
                plt.plot([i,i],[y(x[0]) + (y(x[-1]) - y(x[0])) / (x[-1] - x[0]) * (i - x[0]),f(i)],'r')




x = np.linspace(0, 1)
fig, ax = plt.subplots()
plt.plot(x, f(x), 'b')
for t_i in t:
    plt.plot(t_i, f(t_i), 'bo')
linear_interpolation(t, f)
plt.grid()
plt.show()
