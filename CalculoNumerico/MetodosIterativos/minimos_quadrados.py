from random import *

def randf(n):
    return 2*n*random() -n


def mean(X):
    s = 0.
    n = len(X)
    for i in range(n):
        s += X[i]
    return s/n

n = 100

X = []
Y = []

alpha = 2.67
beta = -8.71

for i in range(n):
    epsilon = randf(100)
    X.append(i)
    Y.append(alpha * i + beta + epsilon)

xBar = mean(X)
yBar = mean(Y)

num = 0.
den = 0.
for i in range(n):
    num += X[i]*(Y[i] - yBar)
    den += X[i]*(X[i] - xBar)

a = num/den
b = yBar - a*xBar

print(a,b)