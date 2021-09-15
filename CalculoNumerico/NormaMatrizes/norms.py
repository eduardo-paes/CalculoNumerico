# Norma da Matriz A conforme algorítmo de Frobenius
def NormaFrobenius(A):
    n = len(A[0])
    s = 0.
    for i in range(n):
        for j in range(n):
            s += A[i][j]*A[i][j]
    return sqrt(s)

# Norma da Matriz A calculando o máximo absoluto da soma da linha
def NormaInfinita(A):
    n = len(A[0])
    s = 0.
    for i in range(n):
        x = 0.
        for j in range(n):
            x += abs(A[i][j])
        if (i == 0 or x > s):
            s = x
    return s

# Norma da Matriz A calculando o máximo absoluto da soma da coluna
def Norma1(A):
    n = len(A[0])
    s = 0.
    for i in range(n):
        x = 0.
        for j in range(n):
            x += abs(A[j][i])
        if (i == 0 or x > s):
            s = x
    return s
