def chessBoardCellColor(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1])) % 2 == 0

    
#solution 2
    # if (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1]))% 2 == 0:
    #     return True
    # else:
    #     return False
    
#solution 3
    # color1 = ((ord(cell1[0]) - ord('A')) + ord(cell1[1]) - ord('1')) % 2 == 0
    # color2 = ((ord(cell2[0]) - ord('A')) + ord(cell2[1]) - ord('1')) % 2 == 0
    # return color1 == color2
    
    
# failed attempt
    # d = ["a", "c", "e", "g", 1, 3, 5, 7]
    # l = ["b", "d", "f", "h", 2, 4, 6, 8]
    
    # cell1 = tuple(cell1)
    # cell2 = tuple(cell2)
    
    # if cell1[0].lower() in d and cell1[1].lower() in d and cell2[0].lower() in d and cell2[1].lower() in d:
    #     return True
    # if cell1[0].lower() in l and cell1[1].lower() in l and cell2[0].lower() in l and cell2[1].lower() in l:
    #     return True
    # if cell1[0].lower() in d and cell1[1].lower() in l and cell2[0].lower() in d and cell2[1].lower() in l:
    #     return True
    # if cell1[0].lower() in l and cell1[1].lower() in d and cell2[0].lower() in l and cell2[1].lower() in d:
    #     return True
    # return False



"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.



For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.



Input/Output

[execution time limit] 4 seconds (py3)

[input] string cell1

Guaranteed constraints:
cell1.length = 2,
'A' ≤ cell1[0] ≤ 'H',
1 ≤ cell1[1] ≤ 8.

[input] string cell2

Guaranteed constraints:
cell2.length = 2,
'A' ≤ cell2[0] ≤ 'H',
1 ≤ cell2[1] ≤ 8.

[output] boolean

true if both cells have the same color, false otherwise.
"""
