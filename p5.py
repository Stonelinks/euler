limit = 20

def is_divisible(n):
  for i in range(limit/2 + 1, limit + 1):
    if n % i != 0:
      return False
  return True

i = limit/2
while not is_divisible(i):
  i += limit/2

print i
