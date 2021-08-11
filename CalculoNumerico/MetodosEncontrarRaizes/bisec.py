from math import *

def f(x):
    return exp(-2*x)+sqrt(3*x)-2.

def bisec():
    a = 0.1         # f(a) < 0
    b = 4.0         # f(b) > 0
    epsilon = 1e-12 # 1 * 10^{-12}

    c = (a+b)/2.
    i = 1

    while abs(b-a) > epsilon:
        print(i, c, abs(f(c)))

        if (f(c) > 0):
            b = c
        else: 
            a = c

        c = (a + b)/2.
        i += 1