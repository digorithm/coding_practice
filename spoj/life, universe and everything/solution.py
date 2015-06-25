#your code goes here

"""
Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.
"""

from guppy import hpy


def solution(l):
    for n in l:
        if (n == 42):
            break
        print n

if __name__ == "__main__":
    h = hpy()
    h.setref()
    solution([x for x in xrange(1,100)])
    print h.heap()
