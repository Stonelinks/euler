import sys

def is_palindrome(s):
  for i in range(len(s)/2):
    if s[i] != s[len(s) - i - 1]:
      return False
  return True

l = []
for i in range(100, 1000):
  for j in range(100, 1000):
    if is_palindrome(str(i*j)):
      l.append(i*j)

print max(l)
