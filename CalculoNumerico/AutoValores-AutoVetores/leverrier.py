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
Retorna o Traço da matriz A.
"""
def Traco(A):
    n = len(A)
    s = 0.
    for i in range(n):
        s += A[i][i]
    return s

"""
Retorna o polinômio característico da matriz A de ordem n.
"""
def Leverrier(A):
    n = len(A)
    p = [ 0. ] * (n+1)
    s = [ 0. ] * (n+1)
    _A = [ [A[i][j] for j in range(n)] for i in range(n) ]
    for k in range(1, n+1):
        s[k] = Traco(_A)
        sum_tmp = 0.
        for i in range(1, k):
            sum_tmp += p[i] * s[k-i]
        p[k] = (s[k] - sum_tmp)/k
        _A = MatMatMul(_A, A)
    return p

"""
Corrige o retorno do método de Leverrier ignorando a posição [0] do vetor resultado x.
"""
def CorrigeRetorno(x):
    n = len(x)
    y = [ 0. ] * (n-1)
    for i in range(1, n):
        y[i-1] = x[i]
    return y

A = [[1., 1., -1.], [0., 0., 1.], [-1., 1., 0.]]
print("Resultado: ", CorrigeRetorno(Leverrier(A)))