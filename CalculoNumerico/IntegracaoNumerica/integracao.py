from math import *

def f(x):
  return exp(x)

'''
Integração tomando por x o valor mais à esquerda.
'''
def int_esq(a, b, N):
  s = 0.
  h = (b-a)/float(N)
  x = a
  for i in range(N):
    s += f(x)
    x += h
  return h*s

'''
Integração tomando por x o valor mais à direita.
'''
def int_dir(a, b, N):
  s = 0.
  h = (b-a)/float(N)
  x = a + h
  for i in range(N):
    s += f(x)
    x += h
  return h*s

'''
Integração tomando por x o valor mais ao meio.
'''
def int_meio(a, b, N):
  s = 0.
  h = (b-a)/float(N)
  x = a + h/2.
  for i in range(N):
    s += f(x)
    x += h
  return h*s

'''
Integração utilizando a regra do trapézio
'''
def int_trapezio(a, b, N):
  s = 0.
  h = (b-a)/float(N)
  x = a
  for i in range(N):
    s += (f(x) + f(x+h))
    x += h
  return (h/2.) * s

'''
Integração utlizando 1/3 de Simpson
'''
def int_simpson_1_3(a, b, N):
  s = 0.
  h = (b-a)/float(N)
  x = a
  for i in range(ceil(N/2)):
    s += f(x) + 4*f(x+h) + f(x+2*h)
    x += 2*h
  return (h/3.) * s

'''
Integração utlizando 3/8 de Simpson
'''
def int_simpson_3_8(a, b, N):
  s = 0.
  h = (b-a)/float(N)
  x = a
  for i in range(ceil(N/3)):
    s += f(x) + 3*f(x+h) + 3*f(x+2*h) + f(x+3*h)
    x += 3*h
  return (3./8.) * h * s

'''
Integração utlizando a regra Boole
'''
def int_boole(a, b, N):
  s = 0.
  h = (b-a)/float(N)
  x = a
  for i in range(ceil(N/4)):
    s += 7*f(x) + 32*f(x+h) + 12*f(x+2*h) + 32*f(x+3*h) + 7*f(x+4*h)
    x += 4*h
  return (4./90.) * h * s

a = 0
b = 1
N = 12000

print("ESQ:       ", abs(int_esq(a, b, N)) - exp(b) + exp(a))
print("DIR:       ", abs(int_dir(a, b, N)) - exp(b) + exp(a))
print("MEIO:      ", abs(int_meio(a, b, N)) - exp(b) + exp(a))
print("TRAP:      ", abs(int_trapezio(a, b, N)) - exp(b) + exp(a))
print("1/3 SIMP:  ", abs(int_simpson_1_3(a, b, N)) - exp(b) + exp(a))
print("3/8 SIMP:  ", abs(int_simpson_3_8(a, b, N)) - exp(b) + exp(a))
print("BOOLE:     ", abs(int_boole(a, b, N)) - exp(b) + exp(a))
