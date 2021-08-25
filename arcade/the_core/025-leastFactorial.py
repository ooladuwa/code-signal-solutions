def leastFactorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
        if f >= n:
            return f
        continue        

  #  f = i = 1
  #   while f < n:
  #       f *= i
  #       i += 1
  #   return f

"""
Given an integer n, find the minimal k such that

k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.

Example

For n = 17, the output should be
leastFactorial(n) = 24.

17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 120.

[output] integer
"""
