n = 600851475143

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

i = 4
while i < n:
  if n % primes(i)[-1] == 0:
    n /= primes(i)[-1]
  i += 1

print n
