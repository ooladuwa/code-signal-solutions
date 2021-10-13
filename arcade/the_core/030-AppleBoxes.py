"""
You have k apple boxes full of apples. Each square box of size m contains m × m apples. You just noticed two interesting properties about the boxes:

The smallest box is size 1, the next one is size 2,..., all the way up to size k.
Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
Your task is to calculate the difference between the number of red apples and the number of yellow apples.

Example

For k = 5, the output should be
appleBoxes(k) = -15.

There are 1 + 3 * 3 + 5 * 5 = 35 yellow apples and 2 * 2 + 4 * 4 = 20 red apples, making the answer 20 - 35 = -15.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer k

A positive integer.

Guaranteed constraints:
1 ≤ k ≤ 40.

[output] integer

The difference between the two types of apples.
"""


"""
Understand:
- k boxes of apples
- each box contains m x m apples
- box sizes range from 1 to k
- odd boxes have yellow apples
- even boxes have red apples
- return difference between number of red and yellow apples

Plan:
- create two variables red and yellow and set them to 0
- boxes at EVEN indexes are red and ODD indexes are yellow
- iterate through the range of 0 - k increasing by 2 each iteration
    - multipy index times itself and append to yellow
- iterate through the range of 1 - k increasing by 2 each iteration
    - multipy index times itself and append to red
- return difference between yellow and red

"""


def appleBoxes(k):
    red = 0
    yellow = 0
    
    for i in range(1, k+1):
        if i % 2 == 0:
            red += (i * i)
        else: 
            yellow += (i * i)
    return red - yellow

    #using list comprehension:
    # return sum([i*i for i in range(2,k+1,2)]) - sum([i*i for i in range(1,k+1,2)])