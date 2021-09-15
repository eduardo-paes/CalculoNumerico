"""
Retorna a soma da matriz A pela matriz B.
"""
def MatMatAdd(A, B):
    n = len(A)
    s = 0.
    R = [ [0.]*n for i in range(n) ]
    for i in range(n):
        for j in range(n):
            s = 0.
            for k in range(n):
                s += A[i][k] + B[k][j]
            R[i][j] = s
    return R

"""
Retorna o produto da matriz A pela matriz B.
"""
def MatMatMul(A, B):
    n = len(A)
    s = 0.
    R = [ [0.]*n for i in range(n) ]
    for i in range(n):
        for j in range(n):
            s = 0.
            for k in range(n):
                s += A[i][k] * B[k][j]
            R[i][j] = s
    return R

"""
Produto da matriz A pelo vetor v.
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
Produto da matriz A pelo vetor v.
"""
def MatVecAdd(A, v):
    n = len(v)
    x = [0.] * n
    for i in range(n):
        s = 0
        for j in range(n):
            s += A[i][j] + v[j]
        x[i] = s
    return x

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
Método Iterativo Linear de Jacobi-Richardson para identificação do vetor x que soluciona a equação Ax = b.
"""
def JacobiRichardson(A, b, epsilon):
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
            s = 0.
            for j in range(n):
                s -= (L[i][j]*x0[j] + R[i][j]*x0[j])
            x[i] = s + b[i]

        if (MaxAbs(VecVecSub(x, x0))/MaxAbs(x) < epsilon):
            x0 = x
            break;
        x0 = x
    return x0

# Main
A = [[10., 2., 1.], [1., 5., 1.], [2., 3., 10.]]
b = [7., -8., 6.]

print("Resultado: ", JacobiRichardson(A, b, 1e-2))
