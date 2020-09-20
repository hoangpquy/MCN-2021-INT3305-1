import math
def giaithua(n):
  if n == 0:
    return 1
  else:
    return n * giaithua(n - 1)
def prop(n, p, r):
  tohop = giaithua(n + r - 1)/(giaithua(r - 1) * giaithua(n))
  return tohop * p ** n

def infoMeasure(n, p, r):
  i = prop(n, p, r)
  return -math.log(i, 2)

def sumProb(N, p, r):
  sum = 0.0
  for i in range(1, N+1):
    sum += prop(i, p, r)
  return sum

def approxEntropy(N, p, r):
  temp = 0.0
  for i in range(1, N+1):
    temp += infoMeasure(i, p, r)
  return temp / N  

sumProb(100, 0.5, 5)