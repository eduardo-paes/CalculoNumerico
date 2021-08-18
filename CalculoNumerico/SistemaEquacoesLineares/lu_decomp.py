from math import *

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

# Multiplicação de matriz por vetor
def mat_vec_mul(A, v):
    n = len(v)
    x = [0.] * n
    for i in range(n):
        s = 0
        for j in range(n):
            s += A[i][j]*v[j]
        x[i] = s
    return x

# Multiplicação de matrizes
def mat_mat_mul(A, B):
    n = len(A[0])
    R = [[0.] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k]*B[k][j]
            R[i][j] = s
    return R

# Decomposição da matriz A nas matrizes L (lower) e U (upper)
def lu_decomp(A):
    n = len(A[0])
    L = [[0.] * n for i in range(n)]
    U = [[0.] * n for i in range(n)]

    for i in range(n):
        L[i][i] = 1.
        for j in range(n):
            if (i <= j):
                S = 0.
                for k in range (i):
                    S += L[i][k]*U[k][j]
                U[i][j] = A[i][j] - S
            else:
                S = 0.
                for k in range (j):
                    S += L[i][k]*U[k][j]
                L[i][j] = (A[i][j] - S)/U[j][j]
    return L, U

A = [[5.,1.,2.], [3.,1.,4.], [1., 1., 3.]]
b = [7., 7., 13.]

L, U = lu_decomp(A)
#print("L: ", L)
#print("U: ", U)
#print("R: ", mat_mat_mul(L, U))
#print("A: ", A)

# Resolve a equação L*U*x = b, fazendo Ux = y
y = solve_inf(L, b)
x = solve_sup(U, y)

# Verifica se resultado obtido é válido
print(mat_vec_mul(A, x))
print(b)