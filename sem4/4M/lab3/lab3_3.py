from numpy import sin, pi

from lab3_2 import GIVEN_POINTS_Y, GIVEN_POINTS_X, lagrange

y_lagrange = lagrange(2, GIVEN_POINTS_X, GIVEN_POINTS_Y)
y_sin = sin(2 * pi)

print(f"{y_lagrange=}\n"
      f"{y_sin=}\n"
      f"delta = {abs(y_lagrange-y_sin)}")