from math import *
from copy import *

import numpy as np

# Soluciona matriz triangular superior
def SolveSup(A, b):
    n = len(b)
    x = [0.] * n
    for i in range(n-1, -1, -1):
        s = 0.
        for j in range(i+1, n):
            s += A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

# Método de Eliminação Gaussiana com Pivoteamento Parcial
def GaussElimPartialPivot(A, b):
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

"""
Norma da Matriz A conforme algorítmo de Frobenius
Também conhecida por norma euclidiana
"""
def NormaFrobenius(A):
    n = len(A[0])
    s = 0.
    for i in range(n):
        for j in range(n):
            s += A[i][j]*A[i][j]

    return sqrt(s)

"""
Calcula a Inversa de A
Fazendo: A*b[i] = I[i], sendo b[i] 
a coluna i da inversa da matriz A
"""
def CalculaInversa(A):
    n = len(A[0])
    invA = [[0.] * n for i in range(n)]

    # Gera matriz identidade
    I = []
    for i in range(len(A)):
        I.append([])
        for j in range(len(A[0])):
            if (i == j):
                I[-1].append(1.)
            else:
                I[-1].append(0.)

    # Percorre A produzindo vetor coluna x
    for i in range(len(A[0])):
        _A = deepcopy(A)
        GaussElimPartialPivot(_A, I[i])
        x = SolveSup(_A, I[i])

        for j in range(len(x)):
            invA[j][i] = x[j]
    
    return invA

"""
Calcula o condicionamento de A
"""
def Condicionamento(A):
    _A = CalculaInversa(A)
    return NormaFrobenius(A)*NormaFrobenius(_A)

def ResultadoComNumpy(A):
    G = np.array(A)
    _G = np.linalg.inv(G)
    g1 = np.linalg.norm(G, 'fro')
    g2 = np.linalg.norm(_G, 'fro')
    print("Cond(A) com Numpy: ", g1*g2)

A = [[1., 4., 1.], [3., 1., -1.], [-5., 13., -22.]]
b = [7, 3, 48]

x = Condicionamento(A)
print("Cond(A): ", x)

ResultadoComNumpy(A)

#A, b = GaussElimPartialPivot(A, b)
#y = SolveSup(A, b)
#print("Solução: ", y)
