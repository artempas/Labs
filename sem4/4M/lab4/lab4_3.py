import fractions

import matplotlib.pyplot as plt
from numpy import log

F = log
DERIVATIVE = lambda x: 1 / x


def epsilon(x: float, h: float) -> float:
    return abs(DERIVATIVE(x) - (F(x + h) - F(x)) / h)


h = tuple(fractions.Fraction(1,(2 ** (i))) for i in range(15))
y = tuple(epsilon(2, float(h_i)) for h_i in h)
assert len(h)==len(y)
for i in range(len(y)):
    print(f'h={h[i]}, epsilon={y[i]}')


fig,ax=plt.subplots()
plt.plot(h,y,'bo')
plt.xlabel('h')
plt.ylabel('epsilon')
plt.grid()
plt.show()
