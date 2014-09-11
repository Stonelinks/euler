def tri(n):
  return sum(range(1, n + 1))

def count_factors(n):
  c = 1
  for i in range(1, n + 1):
    if n % i == 0:
      c += 1
  return c

i = 1
j = 5
while True:
  if count_factors(tri(i)) > j:
    print i, j, tri(i)
    j += 1
  if j == 500:
    break
  i += 1
