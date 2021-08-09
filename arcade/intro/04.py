"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.
"""

"""
Understand:
in an array of integers, each number except the first and the last has two adjacent numbers. My task is to iterate through the elements of the array multiplying adjacent elements and return the largest product.

Plan:
- create a "product" variable(p) and set it to zero
- create "biggestProduct" variable(bP) that determines the product of the first two elements
- iterate through array multiplying adjacent properties. for each iteration, 
    - compare p to bP...if bP is larger than p, reassign the value of p to bP
- after iterating through array, return p to the caller
"""

def adjacentElementsProduct(inputArray):
    p = -sys.maxsize
    for i in range(0, len(inputArray)-1, 1):
        bP = (inputArray[i] * inputArray[i+1])
        if bP > p:
            p = bP
            continue
    return p       