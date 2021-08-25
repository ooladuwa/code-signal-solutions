def absoluteValuesSumMinimization(a):
    min_num = 0
    total = 1000000000000000000
    
    for i in a:
        sums = 0
        for j in a:
            sums += abs(j-i) 
        if sums < total:
            total = sums
            min_num = i
    return min_num

#  sums = {}
    # for num in a:
    #     total = sum([abs(a[i] - num) for i in range(len(a))])
    #     if total in sums:
    #         sums[total] = min(num, sums[total])
    #     else:
    #         sums[total] = num
    #     print(sums)
    # return sums[min(sums)]
    

"""
For a = [2, 4, 7], the output should be absoluteValuesSumMinimization(a) = 4.

for x = 2, the value will be abs(2 - 2) + abs(4 - 2) + abs(7 - 2) = 7.
for x = 4, the value will be abs(2 - 4) + abs(4 - 4) + abs(7 - 4) = 5.
for x = 7, the value will be abs(2 - 7) + abs(4 - 7) + abs(7 - 7) = 8.
The lowest possible value is when x = 4, so the answer is 4.

For a = [2, 3], the output should be absoluteValuesSumMinimization(a) = 2.

for x = 2, the value will be abs(2 - 2) + abs(3 - 2) = 1.
for x = 3, the value will be abs(2 - 3) + abs(3 - 3) = 1.
Because there is a tie, the smallest x between x = 2 and x = 3 is the answer.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

A non-empty array of integers, sorted in ascending order.

Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-106 ≤ a[i] ≤ 106.

[output] integer

An integer representing the element from a that minimizes the sum of its absolute differences with all other elements.
"""
