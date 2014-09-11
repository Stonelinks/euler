n = 2000000

def primes(n):
  # erasthomers
  A = [True for x in range(n)]
  for i in range(2, n/2 + 1):
    if A[i]:
      for j in range(2*i, n, i):
        A[j] = False
  
  l = []
  for i in range(2, n):
    if A[i]:
      l.append(i)
  return l

s = 0
for i in primes(n):
  s += i

print s
