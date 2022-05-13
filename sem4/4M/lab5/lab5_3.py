import numpy as np
from math import pi as real_pi
from lab5_1 import simpson

n=2
EPS=10**(-6)
f=lambda x:1/(1+x**2)
x_n=tuple(np.linspace(0,1,n+1))
y_n=tuple(f(x) for x in x_n)
int_n=simpson(x_n,y_n)
while True:
    x_2n=tuple(np.linspace(0,1,2*n+1))
    y_2n=tuple(f(x) for x in x_2n)
    int_2n=simpson(x_2n,y_2n)
    if abs(int_2n-int_n)/15<EPS:
        break
    y_n=y_2n
    x_n=x_2n
    int_n=int_2n
    n*=2
print(f"Pi={int_2n*4}\ndifference with real pi {abs(int_2n*4-real_pi)}")