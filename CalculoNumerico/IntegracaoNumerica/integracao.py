from math import *

def f(x):
  return exp(x)

'''
Integração tomando por x o valor mais à esquerda.
'''
def int_esq(a, b, N):
  s = 0.
  h = (b-a)/N
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
  h = (b-a)/N
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
  h = (b-a)/N
  x = a + h/2.
  for i in range(N):
    s += f(x)
    x += h
  return h*s

  