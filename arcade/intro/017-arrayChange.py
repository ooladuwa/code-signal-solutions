def arrayChange(inputArray):
    count = 0
    a = inputArray[0]
    for i in inputArray[1:]:
        if i <= a:
            count += a-i+1
            a = a+1
        else:
            a = i
    return count
"""
Understand:
- take in an array of integers
- create an array of strictly increasing integers
- return the total number of changes it took to get there
"""

"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.

[output] integer

The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.
"""