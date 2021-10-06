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
Retorna decomposição LU da matriz A.
"""
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

"""
Retorna a soma absoluta dos elementos da matriz triangular inferior.
"""
def SumAbsTriang(A):
    n = len(A)
    s = 0.
    for i in range(n):
        for j in range(i):
            s += abs(A[i][j])
    return s

"""
Método Rutishauser para identificar os autovalores da matriz A.
"""
def Rutishauser(A, epsilon):
    while(SumAbsTriang(A) > epsilon):
        L, U = DecompLU(A)
        A = MatMatMul(U, L)
    return [ A[i][i] for i in range(len(A)) ]

A = [[2., 0., 1.], [0., 1., 0.], [1., 0., 1.]]
print(Rutishauser(A, 0.0001))