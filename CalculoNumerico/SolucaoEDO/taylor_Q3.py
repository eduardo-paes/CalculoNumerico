def f(x,y):
  return -y + x + 2

def df(x,y):
  return y - x - 1

def ddf(x,y):
  return -y + x + 1

def TaylorQ3():
  h = 0.1
  x = 0
  y = 2

  while (x <= 1.0):
    y = y + h*f(x,y) + ((h**2)/2.)*df(x,y) + ((h**3)/6.)*ddf(x,y)
    x = x + h
    print(x, y)
  
TaylorQ3()