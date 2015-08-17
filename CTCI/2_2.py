"""
Question 2-2. algorithm to find from kth element to last element
of a linked list. It's definitely not optimized, can be way more
improved. But still, it works.

"""

from classes.LinkedList import *

def KthToLastElement(linkedlist, k):

    if k < 0:
        "invalid k"

    ll = []
    currnode = linkedlist.head

    while currnode.next != None:
        ll.append(currnode.value)
        currnode = currnode.next

    ll.append(linkedlist.tail.value)
    length = len(ll)

    result = []

    if k == 0:
        return ll

    if k == 1:
        return ll[1:]

    for i in xrange(k-1, length):
        result.append(ll[i])
   
    return result

ll = randomLinkedList(9,3,7)
print ll

print "10 to last: ", KthToLastElement(ll, 10)
print "9 to last: ", KthToLastElement(ll, 9)
print "8 to last: ", KthToLastElement(ll, 8)
print "5 to last: ", KthToLastElement(ll, 5)
print "0 to last: ", KthToLastElement(ll, 0)
print "1 to last: ", KthToLastElement(ll, 1)







