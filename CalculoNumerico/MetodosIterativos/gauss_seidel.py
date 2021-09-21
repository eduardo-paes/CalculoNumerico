"""
Verifica se a matriz é diagonalmente dominante.
Algoritmo: |A[i][i]| > sum(|A[i][j]|), para i != j.
Retorna True se a matriz é diagonalmente dominante, e False do contrário.
"""
def VerificaMatriz(A):
    n = len(A)
    diag = 0.
    sum = 0.

    for i in range(n):
        diag = abs(A[i][i])
        for j in range(n):
            if (i != j):
                sum += abs(A[i][j])
        if (diag <= sum):
            return False
    return True

"""
Retorna a diferença do vetor x pelo vetor y.
"""
def VecVecSub(x, y):
    n = len(x)
    return [x[i] - y[i] for i in range(n)]

"""
Retorna o máximo absoluto do vetor v.
"""
def MaxAbs(v):
    return max([ abs(v[i]) for i in range(len(v)) ])

"""
Método Iterativo Linear de Gauss-Seidel para identificação do vetor x que soluciona a equação Ax = b.
"""
def GaussSeidel(A, b, epsilon):
    n = len(A)
    G = [[A[i][j] for j in range(n)] for i in range(n)]     # G = A*
    L = [[0.] * n for i in range(n)]                        # Matriz diagonal inferior de G
    R = [[0.] * n for i in range(n)]                        # Matriz diagonal superior de G

    # Gera matriz G correspondente à A*,
    # onde cada linha é dividida pelo elemento da diagonal.
    # L[i]/A[i][i]
    for i in range(n):
        b[i] /= A[i][i]
        for j in range(n):
            if (i != j):
                G[i][j] /= A[i][i]

            # Preenche matriz L com elementos da matriz inferior de G,
            # e preenche matriz R com elementos da matriz superior de G.
            if (j < i):
                L[i][j] = G[i][j]
            elif (j > i):
                R[i][j] = G[i][j]

    # Variáveis utilizadas na iteração
    x0 = [0.] * n

    while (True):
        x = [0.] * n
        for i in range(n):
            s = b[i]
            for j in range(n):
                s -= (L[i][j]*x[j] + R[i][j]*x0[j])
            x[i] = s

        # Para iteração caso não haja convergência
        if (MaxAbs(x0)!= MaxAbs(x0)):
            print("\tMétodo não convergente para a matriz informada.")
            break;

        if (MaxAbs(VecVecSub(x, x0))/MaxAbs(x) < epsilon):
            x0 = x
            break;
        x0 = x
    return x0

# Main
A = [[5.,1.,1.], [3.,4.,1.], [3., 3., 6.]]
b = [5.,6.,0.]

print("Resultado: ", GaussSeidel(A, b, 1e-2))
