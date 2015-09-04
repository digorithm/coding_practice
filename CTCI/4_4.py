
def create_tree(array):
    """
    Helper function that receives a array
    and creates a binary search tree
    """
    if not array:
        return
    mid = (len(array))/2
    node = TreeNode(array[mid])
    node.left = create_tree(array[:mid])
    node.right = create_tree(array[mid+1:])
    return node

class TreeNode:     
         
    def __init__(self,data,left_node=None,right_node=None):
        self.data=data
        self.left=left_node
        self.right=right_node
             
    def traverse(self,func,level=0):
        if self.left:
            self.left.traverse(func, level+1)
        func(self,level)    
        if self.right:
            self.right.traverse(func, level+1)

"""
using python list as linked list, it's trivial to
change it to a real linked list
"""
def create_linked_list():
    d = dict()
    def fillDict(node, level):
        if d.has_key(level):
            l = d[level]
            l.append(node.data)
        else:
            l = [node.data]
            d[level]=l

    bt.traverse(fillDict)

    print d

arr = [1,2,3,4,5,7,9,11,66]

bt = create_tree(arr)

create_linked_list()
