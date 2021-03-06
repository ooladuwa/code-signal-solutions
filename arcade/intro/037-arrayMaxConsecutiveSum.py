def arrayMaxConsecutiveSum(inputArray, k):
    c = m = sum(a[:k])
    
    for i in range(len(a) - k):
        c = c + a[i + k] - a[i]
        m = max(c, m)
        
    return m





#WORKS DON'T UNDERSTAND
   sums = [sum(inputArray[:k])]
    for i in range(1, len(inputArray) - k + 1):
        sums.append(sums[i - 1] - inputArray[i - 1] + inputArray[i + k - 1])
    return max(sums)
   
   


# FAILED ONE HIDDEN TEST
    # result = 0
    # for i in range(len(inputArray) -1):
    #     if sum(inputArray[i:i+k]) > result:
    #         result = sum(inputArray[i:i+k])
    # return result
    
"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Array of positive integers.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
1 ≤ inputArray[i] ≤ 1000.

[input] integer k

An integer (not greater than the length of inputArray).

Guaranteed constraints:
1 ≤ k ≤ inputArray.length.

[output] integer

The maximal possible sum.
"""