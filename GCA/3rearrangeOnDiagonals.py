def rearrangeOnDiagonals(a, corner):



"""
You are given a 2D array a with n rows and m columns, consisting of English lowercase letters and an integer corner specifying one of the four corners of the 2D array a.

corner = 1 corresponds to the top-left corner;
corner = 2 corresponds to the top-right corner;
corner = 3 corresponds to the bottom-right corner;
corner = 4 corresponds to the bottom-left corner.


Now consider the numbering of the elements of a in order from left to right and from up to down like this:



Your task is to rearrange the elements of the array by consecutively putting the numbered elements diagonally starting from the corner specified by corner.

For corner = 1, the following rearranging is expected:



For corner = 2, the following rearranging is expected:


For corner = 3, the following rearranging is expected:


For corner = 4, the following rearranging is expected:


Example

For
a = [["a", "b", "c", "d"],
     ["a", "c", "d", "e"],
     ["a", "e", "c", "a"]]
and
corner = 1, the output should be

rearrangeOnDiagonals(a, corner) = [["a", "c", "c", "a"],
                                   ["b", "a", "e", "c"],
                                   ["d", "d", "e", "a"]]
In this case, we have an 3x4 array and it should be numbered in this way:



Now, since corner = 1 it should become a 2D array with the same dimensions, where the respective elements of the array should be put in this order(diagonally, from bottom-left to top-right).



So the array a:

abcd
acde
aeca
should be transformed to this:

acca
baec
ddea
For
a = [["a", "b", "a"],
     ["b", "a", "b"],
     ["a", "b", "a"],
     ["b", "a", "b"],
     ["a", "b", "a"]]
and
corner = 4, the output should be

rearrangeOnDiagonals(a, corner) = [["b", "b", "a"],
                                   ["a", "a", "a"],
                                   ["b", "b", "b"],
                                   ["a", "a", "a"],
                                   ["a", "b", "b"]]
After rearranging the new array will look as follows:

bba
aaa
bbb
aaa
abb
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.char a

Two-dimensional array of English lowercase letters.

Guaranteed constraints:
1 ≤ a.length ≤ 100,
1 ≤ a[i].length ≤ 100.

[input] integer corner

Guaranteed constraints:
1 ≤ corner ≤ 4.

[output] array.array.char