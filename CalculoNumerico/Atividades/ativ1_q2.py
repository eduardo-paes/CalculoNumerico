from math import *

# Método iterativo linear aplicada à função abaixo
def f(x):
    return e**x  - 3*(x**2)

# Função psi negativa obtida a partir de f(x)
def psi_neg(x):
    return -sqrt((e**x)/3)

# Função psi negativa obtida a partir de f(x)
def psi_pos(x):
    return sqrt((e**x)/3)

# Impressão dos resultados
def print_res(i, x, f):
    print("\tIterações: " + str(i) + "\tx: " + str(x) + "\tf(x) = " + str(f))

# Erro utilizado
err = 1e-8

##### Questão 2a
x = 0.
i = 0
print("## Questão 2a\n\tPara x = 0 usando o valor negativo:")
while (abs(x - psi_neg(x)) > err):
    x = psi_neg(x)
    i += 1
print_res(i, x, f(x))

i = 0
print("\n\tPara x = 0 usando o valor positivo:")
while (abs(x - psi_pos(x)) > err):
    x = psi_pos(x)
    i += 1
print_res(i, x, f(x))

##### Questão 2b
x = 5.
i = 0
print("\n## Questão 2b\n\tPara x = 5, usando o valor negativo:")
while (abs(x - psi_neg(x)) > err):
    x = psi_neg(x)
    i += 1
print_res(i, x, f(x))

i = 0
print("\n\tPara x = 5, usando o valor positivo:")
while (abs(x - psi_pos(x)) > err):
    x = psi_pos(x)
    i += 1
print_res(i, x, f(x))

x = 3.
i = 0
print("\n\tPara x = 3, usando o valor negativo:")
while (abs(x - psi_neg(x)) > err):
    x = psi_neg(x)
    i += 1
print_res(i, x, f(x))

i = 0
print("\n\tPara x = 3, usando o valor positivo:")
while (abs(x - psi_pos(x)) > err):
    x = psi_pos(x)
    i += 1
print_res(i, x, f(x))

# Observa-se que o Método Iterativo Linear não é capaz de encontrar a terceira raiz para a função dada
print("\n\nRaiz próxima de 4,0: valor de x próximo de 3,733\nErro utilizado: 1e-8\n")
