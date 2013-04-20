#!/usr/bin/env python

#class Node:
#    def __init__(self,data=None,left=None,right=None):
#        self.data = data
#        self.left = left
#        self.right = right

class BTree:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

    def insertLeft(self,value):
        self.left = BTree(value)
        return self.left
    
    def insertRight(self,value):
        self.right = BTree(value)
        return self.right

    def show(self):
        print self.data

#inorder traversal
def inorder(node): 
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()
        if node.right:
            inorder(node.right)

#inorder traversal,right first.
def rinorder(node): 
    if node.data:
        if node.right:
            rinorder(node.right)
        node.show()
        if node.left:
            rinorder(node.left)

def insert(node,value):
    if value > node.data:
        if node.right:
            insert(node.right,value)
        else:
            node.insertRight(value)
    else:
        if node.left:
            insert(node.left,right)
        else:
            node.insertLeft(value)

if __name__=='__main__':
    I = [3,4,5,7,20,43,2,15,30]
    Root = BTree(I[0])
    for i in range(1,len(I)):
        insert(Root,I[i])

    print '..................'
    inorder(Root)
    print '..................'
    rinorder(Root)
