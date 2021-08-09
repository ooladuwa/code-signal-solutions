"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.
"""


"""
Understand:
given an array of strings, return new array with values of the longest strings

Plan:
create empty list
create longest variable set to 1
loop through finding length of each string
    if string length > longest
        longest = string length
loop through again
    append strings with length value longest to new array
"""

def allLongestStrings(inputArray):
    new = []
    longest = 0
   
    for i in range(len(inputArray)):
        if len(inputArray[i]) > longest:
           longest = len(inputArray[i])
           
    for j in range(len(inputArray)):
        if len(inputArray[j]) == longest:
            new.append(inputArray[j])
    return new
