def palindromeRearranging(inputString):
    elements = {c:inputString.count(c) for c in set(inputString)}
    even = [e % 2 == 0 for e in elements.values()]
    return all(even) or (len(inputString) % 2 == 1 and even.count(False) == 1)

"""
def palindromeRearranging(inputString): 
    count = 0
    l = len(inputString)
    
    if l == 1:
        return True
            
    if l % 2 == 0:
        for c in inputString:
            if inputString.count(c) % 2 != 0:
                #return False
                return False
    
    elif l % 2 != 0:
        for c in inputString:
            if inputString.count(c) % 2 != 0:
                count += 1
                
    if count > 1:
        return False
    return True
"""


    # create count variable set to zero
    # get length of inputString
    # condition 1:
    # if len == 1 return True
    # condition 2:
    # if len modulo 2 is zero
        # iterate through string getting count for letters
            # if any letter count modulo 2 != zero
                #return False
    # condition 3:
    # if len modulo 2 is not zero
        # iterate through string getting count for letters
            # if any letter count modulo 2 != zero
                # count += 1
                
    # condition 4:
    # count > 1 ? False : True



    """
    Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""
