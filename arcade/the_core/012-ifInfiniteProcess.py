def isInfiniteProcess(a, b):
    if a == b:
        return False
        
    if (max(a, b) - min(a, b)) % 2 == 0 and b != 0 and a < b:
        return False
    return True

"""
Understand:
given two integers, when a is incremented my one and b is decremented by one do they ever reach the same number at the same time
- if difference between a and b is even, output should be false
- if difference between a and b is odd, output should be true
"""


"""
Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

Example

For a = 2 and b = 6, the output should be
isInfiniteProcess(a, b) = false;
For a = 2 and b = 3, the output should be
isInfiniteProcess(a, b) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer a

Guaranteed constraints:
0 ≤ a ≤ 20.

[input] integer b

Guaranteed constraints:
0 ≤ b ≤ 20.

[output] boolean

true if the pseudocode will never stop, false otherwise.
"""