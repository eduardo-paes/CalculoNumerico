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
Método das pontências que retorna o autovalor dominante da matriz A.
"""
def PowerMethod(A, y0, epsilon):
    y = y0
    n = len(y0)
    l = n * [ 0. ]

    z = MatVecMul(A, y)
    l = DivDot(z, y)
    alpha = MaxAbs(z)
    y = MulSc(z, 1./alpha)

    while (True):
        lk = l[0]
        z = MatVecMul(A, y)
        l = DivDot(z, y)
        alpha = MaxAbs(z)
        y = MulSc(z, 1./alpha)

        if (( abs(lk - l[0])/abs(lk) ) < epsilon):
            break
    return lk

A = [[3., 0., 1.], [2., 2., 2.], [4., 2., 5.]]
y0 = [1., 1., 1.]
print("Resultado: ", PowerMethod(A, y0, 1e-8))