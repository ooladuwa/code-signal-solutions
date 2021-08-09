"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-1 ≤ a[i] ≤ 1000.

[output] array.integer

Sorted array a with all the trees untouched.
"""

"""
- given an array, trees are represented by -1. 
- trees can NOT move
- sort all other elements in non-descending order
"""

def sortByHeight(a):
    i = 0
    
    treeless = sorted([num for num in a if num != -1])
    print(treeless)
    
    
    for c in range(len(a)):
        if a[c] == -1:
            pass
        else: 
            a[c] = treeless[i]
            i += 1
    return a
    
    
    # # create empty "immovable" array
    # immovable = []
    # # create "count" variable set to 0
    # count = 0
    # # iterate through array for value -1
    # for i, v in enumerate(a):
    #     # if value at given index == -1
    #     if v == -1:
    #     # append index to immovable
    #         count += 1
    #         immovable.append(i)
    # print(immovable)
    # print(count)
    # # sort array in ascending order
    # aS = sorted(a, reverse=True)
    # a = aS
    # print(a)
    
    # slicedA = sorted(a[:len(a) - count])
    # print(slicedA)
    
    # if len(slicedA) == 0:
    #     slicedA = [-1 for i in range(count)]
    #     return slicedA
        
    # # iterate through immovable
    # for num in immovable:
    # # iterate through sorted array at each index
    #     for i in range(len(slicedA)-1):
    #         if slicedA[i] == num or i == num:
    #             slicedA.insert(i, -1)
    #         else:
    #             continue
    #      # insert -1 at given index
    # return(slicedA)

