def pgcd(a,b):
            a,b = max(a,b),min(a,b)
            r = a%b
            if r == 0: return b
            print("a = {}, b = {}, r = {}".format(a,b,r))
            return pgcd(b,a%b)
    
def pgcd2(a,b):
    while b!=0:
        (a,b) = (b, a%b)
    return a

import string


"""
a = zip(range(26),(string.ascii_lowercase))
print([x for x in a])
"""
