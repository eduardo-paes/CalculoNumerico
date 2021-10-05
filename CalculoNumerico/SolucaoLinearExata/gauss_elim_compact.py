from math import *
from copy import *

def mat_vec_mul(A, v):
    n = len(v)
    x = [0.] * n
    for i in range(n):
        s = 0
        for j in range(n):
            s += A[i][j]*v[j]
        x[i] = s
    return x

def vec_vec_sub(x, y):
    n = len(x)
    r = [x[i] - y[i] for i in range(n)]
    return r

def vec_vec_add(x, y):
    n = len(x)
    r = [x[i] + y[i] for i in range(n)]
    return r

# Norma de um vetor
def norm(x):
    return sum( [abs(x[i]) for i in range(len(x)) ])

# Soluciona matriz triangular superior
def solve_sup(A, b):
    n = len(b)
    x = [0.] * n
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

# Método Gaussiano Compacto
def gauss_elim_compact(A, b):
    n = len(b)
    for k in range(n-1):
        for i in range(k+1, n):
            p = A[i][k]/A[k][k]
            b[i] = b[i] - p * b[k]
            A[i][k] = p
            for j in range(k+1, n):
                A[i][j] = A[i][j] - A[k][j] * p
    return A, b

# Refatora valor de b com relação ao resíduo r
def refactorB(A, b):
    n = len(b)
    for k in range(n-1):
        for i in range(k+1, n):
            p = A[i][k]
            b[i] = b[i] - p * b[k]
    return b

# Função de refinamento da solução
def refinamento(A, b):
    _A = deepcopy(A)
    _b = deepcopy(b)

    A,b = gauss_elim_compact(A,b)
    xBar = solve_sup(A,b)

    r = vec_vec_sub(_b, mat_vec_mul(_A, xBar))
    
    epsilon = 1e-8
    while(norm(r) > epsilon):
        r = refactorB(A,r)
        y = solve_sup(A,r)
        xBar = vec_vec_add(xBar, y)
        r = vec_vec_sub(_b, mat_vec_mul(_A, xBar))

    return xBar

A = [[6.,2.,-1], [2.,4.,1.], [3., 2., 8.]]
b = [7.,7.,13.]

x = refinamento(A, b)
print(x)
