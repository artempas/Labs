from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, pi, cos


def f(x: float) -> float:
    return sin(x * pi)


def first(t: list):
    plot_f(t, f)
    plot_linear_interpol(t, f)
    plt.grid()
    plt.show()



def plot_f(t: list, y):
    # Строит график sin(pi * x) и заданных точек на [0; 1]
    # :param t: узлы интерполяции
    # :param y: сама функция

    x = np.linspace(0, 1)  # создаем точки для оси Х
    fig, ax = plt.subplots()  # создаем поле для рисования

    plt.plot(x, y(x), 'b')  # изображаем функцию

    for t_i in t:
        plt.plot(t_i, y(t_i), 'ro')


def plot_linear_interpol(t: list, y):
    # Строит график линейной интерполяции
    # :param t: узлы интерполяции
    # :param y: функция, приближение которой ищем

    for i in range(len(t) - 1):
        x = np.linspace(t[i], t[i + 1])
        plt.plot(x, y(x[0])+(y(x[-1])-y(x[0]))/(x[-1]-x[0])*(x-x[0]), 'g')


def second(t: list):
    # задание 2

    plot_f(t, f)
    plot_lagrange(n=5, t=t, y=f)

    plt.grid()
    plt.show()


def lagrange(k: int, x: float, t: list) -> float:
    # Ищем значения полинома Лагранжа в точке
    # :param k: номер члена, множитель которого убираем
    # :param x: точка
    # :param t: массив узлов
    # :return: значение полинома

    temp = np.array([x for _ in range(len(t))]) - np.array(t)
    temp[k] = 1
    result = reduce(lambda i, j: i * j, temp)
    return result


def plot_lagrange(n: int, t: list, y):
    # Вычисляет+строит многочлен Лагранжа по заданной степени
    # :param n: степень многочлена
    # :param t: заданные точки
    # :param y: функция, приближение для которой нужно найти

    x = np.linspace(0, 1)
    free_term_matrix = [y(ti) for ti in t]
    result = [sum([lagrange(k, xi, t) * free_term_matrix[k] / lagrange(k, t[k], t) for k in range(len(t))]) for xi in x]
    plt.plot(x, result)


def third(t):
    # задание 3

    free_term_matrix = [f(ti) for ti in t]
    xi = 2
    result = sum([lagrange(k, xi, t) * free_term_matrix[k] / lagrange(k, t[k], t) for k in range(len(t))])
    expected = f(xi)
    print(f"Ожидаем: {expected}. Что получили: {result}. Погрешность: {expected - result}")


def fourth():
    # задание 4

    # x = np.linspace(-5, 5, 20) #тут меняем

    a, b, n = -5, 5, 50  # узлы Чебышёва
    x = np.array([0.5 * (a + b) + 0.5 * (b - a) * cos((2 * k - 1) * pi / (2 * n)) for k in range(1, n + 1)])

    plot_runge(x)

    plt.grid()
    plt.show()


def runge(x: float) -> float:
    # Функция Рунге
    # :param x: точка
    # :return: значение функции

    return 1 / (1 + 25 * x ** 2)


def plot_runge(temp_xs: np.array):
    # График Рунге
    # :param temp_xs: точки для отметки

    x = np.linspace(-5, 5)
    plt.plot(x, runge(x), 'g')

    for temp_x in temp_xs:
        plt.plot(temp_x, runge(temp_x), 'ro')

    x = np.linspace(-5, 5)
    free_term_matrix = [runge(ti) for ti in temp_xs]
    result = [sum([lagrange(k, xi, temp_xs) * free_term_matrix[k] / lagrange(k, temp_xs[k], temp_xs) for k in
                   range(len(temp_xs))]) for xi in x]
    plt.plot(x, result, 'r')


t = [0, 1 / 6, 1 / 3, 1 / 2, 1]
#first(t)
#second(t)
#third(t)
fourth()
