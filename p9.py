import sys

n = 1000

for i in range(1, n):
  for j in range(1, n):
    for k in range(1, n):
      if i**2 + j**2 == k**2 and i + j + k == n:
        print i*j*k
        sys.exit()
