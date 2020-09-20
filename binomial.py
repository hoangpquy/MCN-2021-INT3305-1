import math
def giaithua(n):
  if n == 0:
    return 1
  else:
    return n * giaithua(n - 1)
def prop(n, p, N):
  tohop = giaithua(N)/(giaithua(n) * giaithua(N-n))
  return tohop * p ** N

def infoMeasure(n, p, N):
  i = prop(n, p, N)
  return -math.log(i, 2)

def sumProb(N, p):
  sum = 0.0
  for i in range(1, N+1):
    sum += prop(i, p)
  return sum

def approxEntropy(N, p):
  temp = 0.0
  for i in range(1, N+1):
    temp += infoMeasure(i, p, N)
  return temp / N  