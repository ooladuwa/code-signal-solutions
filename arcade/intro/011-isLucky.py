"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""

"""
Understand:
Given a ticket number, determine if it it lucky. It's lucky if the sum of the first half of digits == sum of second half digits
"""
def isLucky(n):
    result1 = 0
    result2 = 0
    
    # integer version of 1/2 length of n
    h = int(len(str(n))/2)
    
    # integer version of length of n
    f = int(len(str(n)))
    
    # n in string form so it can be listed
    nString = str(n)
    
    # n in list form so it can be sliced
    nList = list(nString)
    
    # n sliced from 0 to 1/2 length
    frontList = (nList[:h])
    
    # n sliced from 1/2 length to length
    rearList = nList[h:f]

    # iterate through front of list
    for n in frontList:
        a = int(n)
        result1 += a
    
    # iterate through rear of list
    for m in rearList:
        b = int(m)
        result2 += b
    
    # compare results and return boolean
    if result1 == result2:
        return True
    else: 
        return False