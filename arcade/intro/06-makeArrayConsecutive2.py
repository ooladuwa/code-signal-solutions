"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer statues

An array of distinct non-negative integers.

Guaranteed constraints:
1 ≤ statues.length ≤ 10,
0 ≤ statues[i] ≤ 20.

[output] integer

The minimal number of statues that need to be added to existing statues such that it contains every integer size from an interval [L, R] (for some L, R) and no other sizes.
"""

"""
Understand:
- given array of numbers, find smallest number and largest number and sequentially find numbers that do not appear in the array from that range
- return the # of numbers

Plan:
- create count variable
- sort statues
- enumerate statues to get an index and a statue
- create conditional for i
"""
def makeArrayConsecutive2(statues):
    result = 0
    statues.sort()
    for i, statue in enumerate(statues):
        if (i < len(statues)-1):
            result += statues[i+1] - statues[i] - 1
    return result
    
    # return max(statues) -  min(statues) - len(statues) + 1