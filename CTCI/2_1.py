from classes.LinkedList import *

def delete_duplicates(linkedlist):
    if (linkedlist.head != None):
        currNode = linkedlist.head
        dic =  {currNode.value: True}
        while currNode.next != None:
            if currNode.next.value in dic:
                currNode.next = currNode.next.next
            else:
                dic[currNode.next.value] = True
                currNode = currNode.next

ll = randomLinkedList(9,3,7)
print ll

delete_duplicates(ll)

print ll
