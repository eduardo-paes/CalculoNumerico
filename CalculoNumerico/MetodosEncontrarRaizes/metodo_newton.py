from math import *

def f(x):
    return exp(-2*x)+sqrt(3*x)-2.

def df(f, x):           # Diferenciação Numérica
    deltax = 1e-10
    return (f(x + deltax) - f(x))/deltax

def newton():
    epsilon = 1e-12     # 1 * 10^{-12}
    x = 4.0
    i = 0
    while abs(f(x)) > epsilon:
        x = x - f(x) / df(f,x)
        i += 1
        print(i,x,f(x))

newton()