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

    # x inicial fornecido pelo enunciado
    x0 = [0.7, -1.6, 0.6]

    while (True):
        x = [0.] * n
        for i in range(n):
            s = b[i]
            for j in range(n):
                s -= (L[i][j]*x0[j] + R[i][j]*x0[j])
            x[i] = s

        if (MaxAbs(VecVecSub(x, x0))/MaxAbs(x) < epsilon):
            x0 = x
            break;
        x0 = x
    return x0

# Main
A = [[10., 2., 1.], [1., 5., 1.], [2., 3., 10.]]
b = [7., -8., 6.]

print("### Questão 3\n# Utilizando o método de Jacobi-Richardson:")
print("\n\tResultado: ", JacobiRichardson(A, b, 1e-2))
print("")

