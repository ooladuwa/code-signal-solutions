"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string picture

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

[output] array.string

The same matrix of characters, framed with a border of asterisks of width 1.
"""

"""
Understand:
- take in array of characters of equal length
- get length of one element of the array
- iterate through array adding "*" to front of array item       and "*" to back of array item
- insert "*" times array item length at start and end of array
"""

def addBorder(picture):
    l = len(picture[0])
    
    picture.append("*" * l)
    picture.insert(0, "*" * l)
    
    for i in range(len(picture)):
        picture[i] = "*" + picture[i] + "*"
    return picture
    
