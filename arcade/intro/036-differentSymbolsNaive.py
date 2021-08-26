def differentSymbolsNaive(s):
    d = {}
    for char in s:
        if char not in d:
            d[char] = []
    return len(d)

    # return len(set(s))


    """
    Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ s.length ≤ 1000.

[output] integer
"""