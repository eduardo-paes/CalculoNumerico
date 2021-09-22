from math import *

def Lagrande(X, x, k):
    num = 1.
    den = 1.
    for i in range(len(X)):
        if (i != k):
            num *= (x - X[i])
            den *= (X[k] - X[i])
        return num / den

def SumPolinomio(X, Y, x):
    s = 0.
    for k in range(len(X)):
        s += Y[k] * Lagrande(X, x, k)
    return s

n = 10
X = [ i for i in range(n) ]
Y = [ sin(i) for i in range(n) ]

x = 0.
while (x <= 9):
    print(x, SumPolinomio(X, Y, x))
    x += 0.1
