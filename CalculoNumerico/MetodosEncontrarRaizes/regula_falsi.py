from math import *

def f(x):
    return exp(-2*x)+sqrt(3*x)-2.

def regula_falsi():
    a = 0.1             # f(a) < 0
    b = 4.0             # f(b) > 0
    epsilon = 1e-12     # 1 * 10^{-12}

    i = 0
    while abs(b - a) / max(abs(b), 1.) > epsilon:
        c = a - (b-a) * f(a)/(f(b) - f(a))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i += 1
        print(i, c, abs(f(c)))

regula_falsi()