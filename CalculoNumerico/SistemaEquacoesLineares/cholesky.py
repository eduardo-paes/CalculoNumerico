from math import *

# Calcula uma matriz G da forma A = G*G(transposta)
# Com isso, é possível obter um x da seguinte forma:
# A = G*G(t) | GG(t)x = b | Gy = b | G(t)x = y
def cholesky(A):
    n = len(A[0])
    G = [[0.] * n for i in range(n)]

    for j in range(n):
        for i in range(j,n):
            if (i == j):
                S = 0.
                for k in range(i):
                    S += G[i][k] * G[i][k]
                if (A[i][i] - S >= 0):
                    G[i][i] = sqrt(A[i][i] - S)
                else:
                    print ("Matriz não é positiva definida")
                    return
            else:
                S = 0.
                for k in range(j):
                    S += G[i][k] * G[j][k]
                G[i][j] = (A[i][j] - S)/G[j][j]
    return G

A = [[4.,2.,-4.], [2.,10.,4.], [-4., 4., 9.]]
b = [7., 7., 13.]

G = cholesky(A)
print(G)
