"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.
"""


# return a boolean re: if a string is a palindrome
    #if a string is equal to itself when reversed it's a palindrome
    #must be lower case
    

#PLAN:
#reverse input string
#ensure that input string is lowercase
#return boolean value to the caller


def checkPalindrome(inputString):
    return inputString == inputString[::-1]
        