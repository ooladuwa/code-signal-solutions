"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
"""

"""
Understand:
- take in an array
- enumerate array to see index and value
- determine if removing one element at a given index will make the array strictly increasing

Plan:
-take in array
-enumerate array
-iterate through
    -if array at index < array at index+1...next index
    -if array[i] > array[i+1]...remove array[i]
    continue
-iterate through new array
    -if array[i] > array[i+1]
        -return false 
-return true
"""
# def almostIncreasingSequence(sequence):
        
#     changes = 0 
         
#     for i in range(len(sequence)-1):
#         if sequence[i] > (sequence[i+1]):
#             # sequence.remove(sequence[i])
#             changes +=1
#             print(changes)
#         if changes > 1:
#             return False
#         elif changes <= 1:
#             if sequence[i] >= (sequence[i+1]):
#                 return False
#             return True
     
#     # for j in range(0, len(sequence)-1):
#     #     print(sequence)
#     #     if sequence[j] >= sequence[j+1]:
#     #         print("stop") 
#     #         return False
#     #     return True
   
def almostIncreasingSequence(sequence):
    s = sequence
    s2 = s[:]
    deleted = 0
    if (len(s) - len(set(s))) > 1:
        return False
    elif len(set(s)) == 1:
        return True
    
    for i in range(len(s)-1):
        if s2[i] < s2[i+1]:
            continue
        else:
            del s[i:i+2]
            deleted += 1
            
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
        
    if deleted > 1:
        return False
    else:
        return True