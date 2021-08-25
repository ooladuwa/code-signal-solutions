"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 9.

[output] integer

The largest integer of length n.
"""

def largestNumber(n):
    result = ""
    m = [9] * n
    # l = "".join(str([9] * n))
    for num in m:
        result += "9"
    return int(result)