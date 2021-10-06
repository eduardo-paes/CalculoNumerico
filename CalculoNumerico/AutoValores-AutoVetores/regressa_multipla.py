X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(X)
cols = rows + 1
A = [cols * [ 1. ]] * (rows)

for i in range(rows):
    for j in range(1,cols):
        A[i][j] = X[i][j-1]
        print(X[i][j-1], A[i][j])

print(A)

# T = [[1.] * n+1] * n
