from math import *

def f(x):
    return x*x - x - 2. # Função principal

def psi(x):
    return x*x-2        # Função psi de f(x)

def raiz_psi(x):
    return sqrt(x + 2)  # Raiz de psi(x)

x = 1.2
e = 1e-8
i = 0

while ( abs( x - raiz_psi(x) ) > e ):
    x = raiz_psi(x)
    i += 1
    print(i, x, f(x))
