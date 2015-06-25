#!/usr/bin/python

import sys

from guppy import hpy

h = hpy()
h.setref()
 
inputs = [[int(x) for x in sys.stdin.readline().split()] for _ in xrange(int(sys.stdin.readline()))] if False else [(2,10),(5,7),(9999985,10000000),(9999937,9999987)]


def sieve_of_era(n):
    primes = [True]*(n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

sieve = sieve_of_era(max(end for _,end in inputs))

print "\n\n".join("\n".join(str(p) for p in xrange(start,end+1) if sieve[p]) for start,end in inputs)
print h.heap()
