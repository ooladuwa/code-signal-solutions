def replaceMiddle(arr):
    l = len(arr)
    half = l//2
    middle = 0
    if l % 2 == 0:
        middle = sum(arr[half-1:half+1])
        del(arr[half-1:half+1])
        arr.insert(half-1, middle)
    return arr


"""
We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;
if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.
Given array arr, your task is to find its middle, and, if it consists of two elements, replace those elements with the value of middle. Return the resulting array as the answer.

Example

For arr = [7, 2, 2, 5, 10, 7], the output should be
replaceMiddle(arr) = [7, 2, 7, 10, 7].

The middle consists of two elements, 2 and 5. These two elements should be replaced with their sum, i.e. 7.

For arr = [-5, -5, 10], the output should be
replaceMiddle(arr) = [-5, -5, 10].

The middle is defined as a single element -5, so the initial array with no changes should be returned.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer arr

The given array.

Guaranteed constraints:
2 ≤ arr.length ≤ 104,
-103 ≤ arr[i] ≤ 103.

[output] array.integer

arr with its middle replaced by a single element, or the initial array if the middle consisted of a single element to begin with.
"""