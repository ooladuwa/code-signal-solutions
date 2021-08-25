def alphabeticShift(inputString):
  # return "".join('a' if c=='z' else chr(ord(c)+1) for c in inputString)

    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    inputString = [i for i in inputString]
    result = []

    for i in range(len(inputString)):
        for j in range(len(alpha)):
            if inputString[i] != alpha[j]:
                continue
            elif inputString[i] == alpha[j] and inputString[i] != "z":
                result.append(alpha[j+1])
            elif inputString[i] == "z":
                result.append("a")
    return "".join(result)


"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.
"""