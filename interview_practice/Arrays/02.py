"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

Guaranteed constraints:
1 ≤ s.length ≤ 105.

[output] char

The first non-repeating character in s, or '_' if there are no characters that do not repeat.
"""


"""
Understand:
given a string of lowercase letters, return the FIRST instance of a letter that does not repeat
"""

def firstNotRepeatingCharacter(s):
    for i, char in enumerate(s):
        if char not in s[:i] and char not in s[i+1:]:
            return char
    return "_"
    
    # newS = ""
    # cCount = [char for char in s if s.count(char) < 2]
    # if not cCount:
    #     return "_"      
    # else:
    #     return cCount[0]
    