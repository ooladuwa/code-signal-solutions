def longestInversionalSubarray(a, b, c):
    for i in range(len(a)):
        if a[i] not in b or a[i] in c:
            continue
            
        s = a[i:i+1]
        # print(s)
        if a[i] in b and a[i] not in c:
            # t = b[i:i+1]
            # print(t)
            continue
        print("returned:", s)
"""
You are given three arrays of integers a, b, and c. Your task is to find the longest contiguous subarray of a containing only elements that appear in b but do not appear in c.

Return this longest subarray. If there is more than one longest subarray satisfying these conditions, return any of these possible subarrays.

Example

For a = [2, 1, 7, 1, 1, 5, 3, 5, 2, 1, 1, 1], b = [1, 3, 5], and c = [2, 3], the output can be longestInversionalSubarray(a, b, c) = [1, 1, 5].

There is no contiguous subarray of length 4 satisfying all the requirements:

a[0..3] = [2, 1, 7, 1] contains the number a[2] = 7, which doesn't appear in b;
a[1..4] = [1, 7, 1, 1] contains the number a[2] = 7, which doesn't appear in b;
a[2..5] = [7, 1, 1, 5] contains the number a[2] = 7, which doesn't appear in b;
a[3..6] = [1, 1, 5, 3] contains the number a[6] = 3, which does appear in c (which is prohibited);
a[4..7] = [1, 5, 3, 5] contains the number a[6] = 3, which does appear in c;
a[5..8] = [5, 3, 5, 2] contains the number a[6] = 3, which does appear in c;
a[6..9] = [3, 5, 2, 1] contains the number a[6] = 3, which does appear in c;
a[7..10] = [5, 2, 1, 1] contains the number a[8] = 2, which doesn't appear in b;
a[8..11] = [2, 1, 1, 1] contains the number a[8] = 2, which doesn't appear in b.
There are two possible contiguous subarrays of length 3 satisfying all the requirements:

a[3..5] = [1, 1, 5]: both numbers 1 and 5 appear in b, and both of these numbers don't appear in c.
a[9..11] = [1, 1, 1]: the number 1 appears in b, and doesn't appear in c.
example

As you can see, the longest consecutive subarrays of a that fulfill the conditions are a[3..5] = [1, 1, 5] and a[9..11] = [1, 1, 1]. Both of these answers are acceptable.

For a = [1, 2, 3], b = [], and c = [], the output should be longestInversionalSubarray(a, b, c) = [].

Since b is empty, there are no elements that appear in b and not c. So the answer is [].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

The first array of integers.

Guaranteed constraints:
0 ≤ a.length ≤ 105,
-109 ≤ a[i] ≤ 109.

[input] array.integer b

The second array of integers.

Guaranteed constraints:
0 ≤ b.length ≤ 105,
-109 ≤ b[i] ≤ 109.

[input] array.integer c

The third array of integers.

Guaranteed constraints:
0 ≤ c.length ≤ 105,
-109 ≤ c[i] ≤ 109.

[output] array.integer

Any of the longest contiguous subarrays of a which consists only of elements from b that don't appear in c.
"""

