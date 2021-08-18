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
        s = 0.
        for j in range(i+1, n):
            s += A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

# Método Gaussiano com Pivoteamento Parcial
def gauss_elim_partial_pivot(A, b):
    n = len(b)
    for k in range(n-1):
        # Buscar o maior da coluna
        idx_max = k
        max_value = abs(A[k][k])
        for i in range(k+1,n):
            if (abs(A[i][k]) > max_value):
                idx_max = i
                max_value = abs(A[i][k])
        
        # Trocar a linha k por idx_max
        if (k!= idx_max):
            t = b[idx_max]
            b[idx_max] = b[k]
            b[k] = t
            for i in range(n):
                t = A[idx_max][i]
                A[idx_max][i] = A[k][i]
                A[k][i] = t

        for i in range(k+1, n):
            p = A[i][k]/A[k][k]
            b[i] = b[i] - p * b[k]
            A[i][k] = 0.
            for j in range(k+1, n):
                A[i][j] = A[i][j] - A[k][j] * p
    return A, b

A = [[5.,1.,2.], [3.,1.,4.], [1., 1., 3.]]
b = [7.,7.,13.]

A,b = gauss_elim_partial_pivot(A,b)
x = solve_sup(A,b)

print(x)