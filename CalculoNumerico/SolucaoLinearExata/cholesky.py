from math import *

"""
Transposição da matriz A.
"""
def Transposicao(A):
    n = len(A)
    T = [[0.] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            T[i][j] = A[j][i]
    return T

"""
Soluciona matriz triangular inferior
"""
def SolveInf(A, b):
    n = len(b)
    x = [0.] * n
    for i in range(n):
        s = 0
        for j in range(i):
            s += A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

"""
Soluciona matriz triangular superior
"""
def SolveSup(A, b):
    n = len(b)
    x = [0.] * n
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

"""
Calcula uma matriz G da forma A = G*G(transposta)
Com isso, é possível obter um x da seguinte forma:
A = G*G(t) | GG(t)x = b | Gy = b | G(t)x = y
"""
def Cholesky(A, b):
    n = len(A[0])
    G = [[0.] * n for i in range(n)]

    # Cálcula matriz G da forma A = G*G(t) 
    for j in range(n):
        for i in range(j,n):
            S = 0.
            if (i == j):
                for k in range(i):
                    S += G[i][k] * G[i][k]
                if (A[i][i] - S >= 0):
                    G[i][i] = sqrt(A[i][i] - S)
                else:
                    print ("Matriz não é positiva definida")
                    return
            else:
                for k in range(j):
                    S += G[i][k] * G[j][k]
                G[i][j] = (A[i][j] - S)/G[j][j]

    # Cálculo de y fazendo: G*y = b
    y = SolveInf(G, b)

    # Cálculo de x fazendo: G(t)*x = y
    x = SolveSup(Transposicao(G), y)

    return x

# Main
A = [[4.,2.,-4.], [2.,10.,4.], [-4., 4., 9.]]
b = [0., 6., 5.]

print("Resultado: ", Cholesky(A, b))
