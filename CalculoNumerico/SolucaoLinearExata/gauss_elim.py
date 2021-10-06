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

# Método Gaussiano
def gauss_elim(A, b):
    n = len(b)
    for k in range(n-1):
        for i in range(k+1, n):
            p = A[i][k]/A[k][k]
            b[i] = b[i] - p * b[k]
            A[i][k] = 0
            for j in range(k+1, n):
                A[i][j] = A[i][j] - A[k][j] * p
    return A, b

A = [[6.,2.,-1], [2.,4.,1.], [3., 2., 8.]]
b = [7.,7.,13.]

A,b = gauss_elim(A,b)
x = solve_sup(A,b)

print(x)