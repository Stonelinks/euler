def fib(n):
  if n <= 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

s = 0
i = 0
while fib(i) < 4000000:
  if fib(i) % 2 == 0:
    s += fib(i)
  i += 1

print s
