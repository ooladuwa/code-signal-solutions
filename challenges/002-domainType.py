def domainType(domains):
    r = []
    a, a1="organization", ".org"
    b, b1="commercial", ".com"
    c, c1="network", ".net"
    d, d1="information", "info"
    for i in range(len(domains)):
        x = domains[i]
        y = x[len(x)-4:]
        if y == a1:
            r.append(a)
        elif y == b1:
            r.append(b)
        elif y == c1:
            r.append(c)
        elif y == d1:
            r.append(d)
    return r

"""
GoDaddy makes a lot of different top-level domains available to its customers. A top-level domain is one that goes directly after the last dot ('.') in the domain name, for example .com in example.com. To help the users choose from available domains, GoDaddy is introducing a new feature that shows the type of the chosen top-level domain. You have to implement this feature.
To begin with, you want to write a function that labels the domains as "commercial", "organization", "network" or "information" for .com, .org, .net or .info respectively.
For the given list of domains return the list of their labels.

Example

For domains = ["en.wiki.org", "codesignal.com", "happy.net", "code.info"], the output should be
domainType(domains) = ["organization", "commercial", "network", "information"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string domains

A list of domains, where each domain contains at least one dot. It is guaranteed that each top-level domain of these domains belongs to one of the types described above.

Guaranteed constraints:
4 ≤ domains.length ≤ 25,
5 ≤ domains[i].length ≤ 20.

[output] array.string

The list of labels for the given domains.
"""