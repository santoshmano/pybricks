#!/bin/python

import sys

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(data):
    def deserialize():
        val = next(vals,None)
        if val == None:
            return None
        if val == '#':
            return None
        node = Node(int(val))
        node.left = deserialize()
        node.right = deserialize()
        return node
    vals = iter(data.split())

    return deserialize()

def printInorder(root):
    if root == None:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)



def  cloneTree(root):
    if root == None:
        return None

    clone = Node(root.val)
    print(root.val, root, root.left, root.right)
    clone.left = cloneTree(root.left)
    clone.right = cloneTree(root.right)

    return clone




_size = 47
_str = "89 110 93 162 83 100 # # 204 # # 69 199 # # 181 # # # 184 161 143 6 # # 13 # # # # 62 150 # # 168 114 247 # # 186 85 # # 204 # # #"
root = createTree(_str);
printInorder(root);
clone = cloneTree(root);
#printInorder(clone);
