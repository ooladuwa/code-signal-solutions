"""
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example

For a = [50, 60, 60, 45, 70], the output should be
alternatingSums(a) = [180, 105].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
45 ≤ a[i] ≤ 100.

[output] array.integer
"""

"""
Understand:
- take in array of positive integers
- create two variables starting at zero
- iterate through array
    - if index i, add num to count 1
    - if index i+1, add num to count 2
return list count1 / 2, count2 / 2
"""

def alternatingSums(a):
    y = 0
    z = 0
    sums = []
    
    y = [a[i] for i in range(0, len(a), 2)]     
    sums.append(sum(y))
    
    z = [a[j] for j in range(1, len(a), 2)]  
    sums.append(sum(z))
    
    return sums