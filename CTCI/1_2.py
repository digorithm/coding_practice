"""
CTCI - Question 1.2:
Implementing an algorithm to reverse a string;

explanation: I'm not using any python's tricks (s[::-1])

I'm just interating the original string backwards, using its index
to append the original string in position [index] in the new list
"""

def reverse(s):
    l = []
    for i in xrange(len(s)-1,-1,-1):
        l.append(s[i])
    return ''.join(l)

if __name__ == '__main__':
    print reverse('abcd')
    print reverse('rodrigo')
    print reverse('arara')
    print reverse('lol')

