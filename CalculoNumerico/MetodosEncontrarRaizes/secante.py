from math import *

def f(x):
    return exp(-2*x)+sqrt(3*x)-2.

def secante():
    epsilon = 1e-12
    x1 = 6.2
    x2 = 1.8

    i = 1
    while abs(x2 - x1) > epsilon:
        a = (f(x2)-f(x1))/(x2-x1)
        b = f(x1)-a*x1
        x3 = -b/a

        x1 = x2
        x2 = x3
        i += 1

        print(i, x3, abs(f(x3)))

secante()