from math import *

def F(x, N):
    return x*x - N

def raiz_quadrada(N):
    epsilon = 1e-12

    x1 = 0
    x2 = N

    i = 1
    x3 = 0.
    while abs(x2 - x1) > epsilon:
        a = (F(x2, N) - F(x1, N))/(x2-x1)
        b = F(x1, N) - a*x1
        x3 = -b/a

        x1 = x2
        x2 = x3
        i =+ 1

    return x3

res = raiz_quadrada(144)
print(res)