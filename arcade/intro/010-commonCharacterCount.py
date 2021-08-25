"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer
"""


"""
Understand:
- given two strings, return a count of the characters that appear in both strings
    - duplicate characters that appear in both strings must be accounted for individually

Plan:
create newS1 and newS2 as dictionaries
iterate through string creating a new x object
    
    transform each count list into a set
    compare item from one set to item in the other and if they match, return the one with the lower value
"""

def commonCharacterCount(s1, s2):
    A = {x: sum(len(i) for i in s1 if x == i) for x in list(s1)}
    B = {x: sum(len(i) for i in s2 if x == i) for x in list(s2)}
    
    a = 0
    
    common = (set(A) & set(B))
    print(common) 

  
    for char in common:
        if char in A:
            a += min(A[char], B[char])
        
    return a
    
