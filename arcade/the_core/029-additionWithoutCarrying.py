"""
A little child is studying arithmetic. They have just learned how to add two integers, written one below another, column by column. But the child always forgets about the important part - carrying.

Given two integers, your task is to find the result that the child will get.

Note: The child had learned from this site, so feel free to check it out too if you are not familiar with column addition.

Example

For param1 = 456 and param2 = 1734, the output should be
additionWithoutCarrying(param1, param2) = 1180.

   456
  1734
+ ____
  1180
The child performs the following operations from right to left:

6 + 4 = 10 but the child forgets about carrying the 1 and just writes down the 0 in the last column
5 + 3 = 8
4 + 7 = 11 but the child forgets about the leading 1 and just writes down 1 under 4 and 7.
There is no digit in the first number corresponding to the leading digit of the second one, so the child imagines that 0 is written before 456. Thus, they get 0 + 1 = 1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer param1

A non-negative integer.

Guaranteed constraints:
0 ≤ param1 < 105.

[input] integer param2

A non-negative integer.

Guaranteed constraints:
0 ≤ param2 < 6 · 104.

[output] integer

The result that the little child will get by using column addition without carrying.
"""



def additionWithoutCarrying(param1, param2):
    res = 0
    place = 1
    digit_sum = 0 
    
    while param1 or param2:
        #isolate first digit
        digit_sum = ((param1 % 10) + (param2 %10))
        #handle no-carry rule
        digit_sum = digit_sum % 10
        
        #update result
        res = digit_sum * place + res
        #update param1 and param2
        param1 = math.floor(param1/10)
        param2 = math.floor(param2/10)
        #update place
        place = place * 10
    return res
        
"""
Plan:
- create variables for res(result), place(place value), and digit_sum(sum of each iteration of digit sums)
- intialize while loop to while param1 or param2
- isolate first digit by using modulo of 10 on each and adding
- handle no-carrying rule by digit_sum % 10
- res = digit_sum * place + res
- increment place by multiplying by 10
- return res outside of while loop
"""