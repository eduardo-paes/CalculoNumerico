# Com ajuste Polinomial
from random import *
from math import *

### ====== LU DECOMP & UTILS

# Soluciona matriz triangular superior
def SolveSup(A, b):
    n = len(b)
    x = [0.] * n
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

# Soluciona matriz triangular inferior
def SolveInf(A, b):
    n = len(b)
    x = [0.] * n
    for i in range(n):
        s = 0
        for j in range(i):
            s += A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

# Multiplicação de matriz por vetor
def MatVecMul(A, v):
    n = len(v)
    x = [0.] * n
    for i in range(n):
        s = 0
        for j in range(n):
            s += A[i][j]*v[j]
        x[i] = s
    return x

# Multiplicação de matrizes
def MatMatMul(A, B):
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
def DecompLU(A):
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

### ====== MINQUAD

# Potência de (X**j) * Y
def PowerX_Y(X, j, Y):
  s = 0.
  for i in range(len(X)):
    s += (X[i]**j) * Y[i]
  return s

# Retorna y += _a[i] * (x**i), sendo i de 0 à len(_b)
def PowerA_X(_b, x):
  y = 0.
  for i in range(len(_b)):
    y += _b[i]*(x**i)
  return y

# Retorna A e b
def MinQuad_Questao3b(_b, n):
  k = len(_b) - 1
  X = []
  Y = []

  # Calcula X e Y auxiliares
  for x in range(n):
    X.append(x)
    # y = sum(_b[i]*(x**i))
    Y.append(PowerA_X(_b, x))

  # Calcula b
  b = [0.] * (k+1)
  for j in range(k+1):
    b[j] = PowerX_Y(X, j, Y)

  # Calcula A
  powerX = [ sum([ X[j]**i for j in range(n) ]) for i in range (2*k + 1) ]
  A = [[0.]*(k+1) for i in range(k+1)]
  for x in range(k+1):
    for j in range(k+1):
      A[x][j] = powerX[x+j]

  return A, b

### ====== MAIN

# Realiza cálculo com mínimos quadrados
_b = [7.3, -2.5, 5.2, -8.6]
n = 50
A, b = MinQuad_Questao3b(_b, n)

# Resolução com LU
L, U = DecompLU(A)
x = SolveSup(U, SolveInf(L, b))

# x deve ser próximo ao valor de entrada em _b
print("Valor de b: ", x)