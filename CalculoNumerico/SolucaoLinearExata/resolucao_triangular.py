from math import *

def mat_vec_mul(A, v):
    n = len(v)
    x = [0.] * n
    for i in range(n):
        s = 0
        for j in range(n):
            s += A[i][j]*v[j]
        x[i] = s
    return x

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

# Soluciona matriz triangular inferior
def solve_inf(A, b):
    n = len(b)
    x = [0.] * n
    for i in range(n):
        s = 0
        for j in range(i):
            s += A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

A = [[1.,2.,-2], [0.,2.,-3.], [0., 0., 1]]
b = [1.,3.,4.]

x = solve_sup(A,b)
print(x)

# Prova Real
print(mat_vec_mul(A, x))
print(b)