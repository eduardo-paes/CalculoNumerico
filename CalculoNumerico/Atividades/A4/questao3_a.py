from math import *

### ====== UTILS

# Multiplicação de matriz por vetor
def MatVecMul(A, v):
    n1 = 0.
    n2 = 0.

    if (len(A) == len(v)):
      n1 = len(A[0])
      n2 = len(v)
    else:
      n1 = len(v)
      n2 = len(A[0])

    x = [0.] * n1

    for i in range(n1):
      s = 0
      for j in range(n2):
        s += v[j] * A[j][i]
      x[i] = s
    return x

# Multiplicação de escalar por vetor
def VecEscMul(Esc, v):
  return [ Esc * v[i] for i in range(len(v)) ]

# Multiplicação de matrizes
def MatMatMul(A, B):
    n = len(A)
    R = [[0.] * len(A) for i in range(len(B[0]))]

    for i in range(n):
      for j in range(len(B[0])):
        s = 0
        for k in range(len(A[0])):
          s += A[i][k] * B[k][j]
        R[i][j] = s
    return R

# Transposição do vetor X.
def Transposicao(A):
    n = len(A)
    T = [[0.] * n for i in range(len(A[0]))]
    for i in range(len(A[0])):
      for j in range(n):
        T[i][j] = A[j][i]
    return T

### ====== MAIN

# Mínimos Quadrados adaptado à questão 3a
# x(t) * x * B = x(t) * Y
# Fazendo A = x(t) * x e b = x(t) * Y
def MinQuad_Questao3a(x, y):
  T = Transposicao(x)
  A = MatMatMul(T, x)
  b = MatVecMul(T, y)
  return A, b

X = [[1.1], [-2.3], [3.5], [-4.6], [5.7]]
Y = [4.2]
A, b = MinQuad_Questao3a(X, Y)

# Para o caso em específico
# A = valor escalar
n = len(b)
x = [0.] * n
for i in range(n):
  x[i] = b[i]/A[0][0]
print("Valor de b: ", x)