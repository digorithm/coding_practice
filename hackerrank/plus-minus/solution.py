"""
You're given an array containing integer values. You need to print the fraction of count of positive numbers, negative numbers and zeroes to the total numbers. Print the value of the fractions correct to 3 decimal places.
"""

from __future__ import division

def main_function(numbers):
    """
    it receives an array of numbers and output the fractions
    """
    total = len(numbers)
    pos = len([x for x in numbers if x>0])
    neg = len([x for x in numbers if x<0])
    z = len([x for x in numbers if x == 0])
    return pos/total, neg/total, z/total

n = raw_input()
vet = raw_input().split()
vet = map(int, vet)
pos, neg, z = main_function(vet)
print ("%.3f" % pos)
print ("%.3f" % neg)
print ("%.3f" % z)
