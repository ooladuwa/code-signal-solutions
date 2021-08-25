"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

Guaranteed constraints:
0 ≤ inputString.length ≤ 50.

[output] string

Return inputString, with all the characters that were in parentheses reversed.
"""

"""
given a string, reverse the contents of anything in parentheses and return the string with reversed content substituted
"""

def reverseInParentheses(inputString):
    new = []
    x = ''
    for i, l in enumerate(inputString):
        print(i,l)
        if (l == "("):
            new.append(x)
            x = ""
            print(new)
        elif (l == ")"):
            x = new.pop() + x[::-1]
            print(new)
            print(x)
        else:
            x += l
            print(x)
    if not x == "":
        new.append(x)
    return "".join(new)
    
    
    
    
    
    
    # find binary of "(" and ")"
    # create list comprehension that turns any "(" or ")into binary
    # reassign indexes at    
    
    # new = []
    # s = list(inputString)
    # # print(s)
    # y=0
    # z=0
    # r=[]
    # ns = ""
    # for i in range(len(s)):
    #     if ord(s[i]) == 40:
    #         y = i
    #         # print(y)
    #     if ord(s[i]) == 41:
    #         z = i
    #         r = s[y+1:z]
    #         r = r[::-1]
    #         s[y+1:z] = r
    #         print("break")
    #         print(s)
    # inputString = s
    # print(type(inputString))
    
    # for i in range(len(inputString)):
    #     # print(ord(inputString[i]))
    #     if inputString[i] != "(" and inputString[i] != ")":
    #         ns += inputString[i]
    
    # for i in range(len(ns)):
    #     if ns[i] == "(":
    #         ns.remove(ns[i])
    # return ns 
            
    #     #     inputString.remove(inputString[i])
    #     #     continue
    #     # if ord(inputString[i]) == 41:
    #     #     inputString.remove(inputString[i])
    #     #     continue
    #     # # if char == ')':
    #     # #     inputString.remove(char)

    # # return "".join(inputString)
    #         # "".join(str(s))
    #         # r = "".join(r)
    #     # for char in inputString:
        
    #     # change to string
    #     # find substring that was originally sliced
    #     # replace substring with r
    # # for i in range(len(s)):
        
    # # return inputString
    #         # s[y+1:z] = r
    #         # ss = str(s)
    #         # print(("".join(ss)))
