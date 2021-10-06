"""
Transposição da matriz A.
"""
def TransposicaoMatriz(A):
    n = len(A)
    T = [[0.] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            T[i][j] = A[j][i]
    return T

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
Divisão ponta-a-ponta entre dois vetores (v,w).
"""
def DivDot(v, w):
    n = len(v)
    return [ v[i]/w[i] for i in range(n) ]

"""
Retorna o máximo absoluto do vetor v.
"""
def MaxAbs(v):
    return max([ abs(v[i]) for i in range(len(v)) ])

"""
Retorna o produto de v pelo escalar sc.
"""
def MulSc(v, sc):
    return [ sc * v[i] for i in range(len(v)) ]

"""
Retorna a diferença do vetor x por pelo vetor y.
"""
def VecVecSub(x, y):
    return [x[i] - y[i] for i in range(len(x))]

"""
Retorna a soma do vetor x por pelo vetor y.
"""
def VecVecAdd(x, y):
    return [x[i] + y[i] for i in range(len(x))]