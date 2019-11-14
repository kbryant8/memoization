from part1 import memoize
from part2 import memoize_aspect
import timeit

def fib(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1

  return memoize(fib, n-1) + memoize(fib, n-2)


@memoize_aspect
def fib2(n):
  print(n)  # uncomment this to see if you did it
  if n == 0:
    return 1
  elif n == 1:
    return 1

  return fib2(n-1) + fib2(n-2)

