"""
Define an integer's roundness as the number of trailing zeroes in it.

Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.

Example

For n = 902200100, the output should be
increaseNumberRoundness(n) = true.

One of the possible ways to increase roundness of n is to swap digit 1 with digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.

For instance, one may swap the leftmost 0 with 1.

For n = 11000, the output should be
increaseNumberRoundness(n) = false.

Roundness of n is 3, and there is no way to increase it.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive integer.

Guaranteed constraints:
100 ≤ n ≤ 109.

[output] boolean

true if it's possible to increase n's roundness, false otherwise.
"""


"""
Understand:
- roundness = # of trailing zeroes following integer
- take in an integer n
-- task is to check if roundness of n can be increased by swapping some pair of digits (digit DO NOT have to be adjacent)

Plan:
- instantiate while loop to determine if there are zeroes at the end of n. while n % 10 == 0  
    - reassign value of n to n/10. Use math.floor
- turn n into a string
- if len(n) == 1 
    - return false
- if len(n) > 1
    - iterate through n:
        if num != 0
            continue
        else
            return true
    return false
"""


def increaseNumberRoundness(n):
    while n % 10 == 0:
        n = math.floor(n / 10)
    print(n)
    n = str(n)
    
    if len(n) == 1:
        return False
    if len(n) > 1:
        for num in n:
            if num == "0":
                return True
            elif num != "0":
                continue
        return False

    
