def tri(n):
  r = 0
  for i in range(1, n + 1):
    r += i
  return r

def count_factors(n):
  c = 1
  for i in range(1, n + 1):
    if n % i == 0:
      c += 1
  return c

print count_factors(28)
