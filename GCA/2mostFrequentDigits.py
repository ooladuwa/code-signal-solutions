def mostFrequentDigits(a):






#Tests
# a: [25, 2, 3, 57, 38, 41] ==> [2, 3, 5]
# a: [90, 81, 22, 36, 41, 57, 58, 97, 40, 36] ==> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a: [28, 12, 48, 23, 76, 64, 65, 50, 54, 98]  ==> [2, 4, 5, 6, 8]

"""
Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.

Example

For a = [25, 2, 3, 57, 38, 41], the output should be mostFrequentDigits(a) = [2, 3, 5].

Here are the number of times each digit appears in the array:

0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1
The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of positive integers.

Guaranteed constraints:
1 ≤ a.length ≤ 103,
1 ≤ a[i] < 100.

[output] array.integer

The array of most frequently occurring digits, sorted in ascending order.
"""
