import math
def prop(n, p):
  return p**n

def infoMeasure(n, p):
  i = prop(n, p)
  return -math.log(i, 2)

def sumProb(N, p):
  sum = 0.0
  for i in range(1, N+1):
    sum += prop(i, p)
  return sum

def approxEntropy(N, p):
  temp = 0.0
  for i in range(1, N+1):
    temp += infoMeasure(i, p)
  return temp / N  

  