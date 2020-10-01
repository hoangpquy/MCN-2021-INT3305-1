import math
def prop(n, p):
  return 1.0*p*(1-p)**(n-1)

def infoMeasure(n, p):
  i = prop(n, p)
  return -math.log(i, 2)

def sumProb(N, p):
  '''
  Khi chay lan luot cac gia tri cua N tu 1 den 100,
  ta duoc sumProb co gia tri xap xi 1
  '''
  sum = 0.0
  for i in range(1, N+1):
    sum += prop(i, p)
  return sum

def approxEntropy(N, p):
  temp = 0.0
  for i in range(1, N+1):
    temp += infoMeasure(i, p) * prop(i, p)
  return temp

for i in range(1, 100): 
  print(sumProb(i, 0.5))

help(sumProb)