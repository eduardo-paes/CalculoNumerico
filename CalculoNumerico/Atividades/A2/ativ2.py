from math import *
from copy import *

"""
Multiplicação de Matriz por Vetor
"""
def MatVecMul(A, v):
    n = len(v)
    x = [0.] * n
    for i in range(n):
        s = 0
        for j in range(n):
            s += A[i][j]*v[j]
        x[i] = s
    return x

"""
Subtração de dois vetores
"""
def VecVecSub(x, y):
    n = len(x)
    r = [x[i] - y[i] for i in range(n)]
    return r

"""
Soma de dois vetores
"""
def VecVecAdd(x, y):
    n = len(x)
    r = [x[i] + y[i] for i in range(n)]
    return r

"""
Norma Infinita de um vetor (x)
"""
def NormaInf(x):
    s = 0.
    for i in range(len(x)):
        s += abs(x[i])
    return s

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
Método Gaussiano com Pivoteamento Parcial
"""
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
Refatora valor de b com relação ao resíduo r
Fazendo: r = b - Ax
"""
def RefactorB(A, b):
    n = len(b)
    for i in range(n-1):
        for j in range(i+1, n):
            b[j] = b[j] - A[j][i] * b[i]
    return b

"""
Função de refinamento da solução.
Considera a seguinte formulação: A(x + y) = b, onde y consiste no erro de x.
Logo o refinamento consiste num método iterativo que procura corrigir o valor 
de x com base no resíduo r dado por: Ay = b - Ax, onde r = b - Ax.
"""
def Refinamento(A, b):
    cpA = deepcopy(A)
    cpb = deepcopy(b)

    # Encontra primeiro valor de x
    A,b = GaussElimPartialPivot(A,b)
    _x = SolveSup(A,b)

    # Calculo do primeiro resíduo
    r = VecVecSub(cpb, MatVecMul(cpA, _x))
    
    # Erro utilizado
    epsilon = 1e-8
    while(NormaInf(r) > epsilon):
        r = RefactorB(A,r)                      # Obtém novo valor de b com relação a r
        y = SolveSup(A,r)                       # Identifica novo valor x dado por y, fazendo: Ay = r
        _x = VecVecAdd(_x, y)                   # Adiciona erro ao valor de x
        r = VecVecSub(cpb, MatVecMul(cpA, _x))    # Fazendo: r = b - Ax

    return _x

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

# Matriz A e valor de B para exemplo
A = [[1.,4.,1.], [3.,1.,-1.], [-5., 13., -22.]]
b = [7.,3.,48.]
cpA = deepcopy(A)

# Resultado do condicionamento de A
print("Número de Condicionamento de A: ", Condicionamento(A))

# Resultado refinado de x
x = Refinamento(A, b)
print("\nValor de x encontrado: ",  x)
print("\nProva real (Ax = b): ",  MatVecMul(cpA,x))
