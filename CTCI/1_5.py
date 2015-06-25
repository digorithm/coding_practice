#!/usr/bin/env python

"""
Write a method to replace all spaces in a string with %20.

"""

def fillSpaces(str):
    chs = list(str)
    for i, ch in enumerate(chs):
        if ch == ' ':
            chs[i] = '%20'
    return ''.join(chs)

"""
Explanation:
    It could be done with regex, but this way is more fun.
    You can't change a string, so you turn it into a list
    of chars and change where the char in given position is
    a space

"""


if __name__ == '__main__':
    print "### Solution of question 1-5 ###"
    print ' '
    print 'Write a method to replace all spaces in a string with %20'
    print ' '
    print 'insert a string:'
    str = raw_input()
    print 'output: ', fillSpaces(str)

