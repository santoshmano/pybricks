import sys

class BinNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def is_leaf(root):
    return True if root.left is None and root.right is None else False

def is_bst(root):
    return _is_bst(root, -sys.maxsize, sys.maxsize)

def _is_bst(root, min, max):

    if root == None:
        return True

    # learning - i had is_leaf() check before this which was wrong
    if root.val <= min or root.val > max:
        return False

    return _is_bst(root.left, min, root.val) and \
           _is_bst(root.right, root.val, max)


root = None
assert(is_bst(root) == True)

root = BinNode(25)
assert(is_bst(root) == True)

root = BinNode(25)
root.left = BinNode(15)
root.right = BinNode(35)
root.left.left = BinNode(10)
root.left.right = BinNode(20)
root.right.left = BinNode(30)
root.right.right = BinNode(40)
assert(is_bst(root) == True)

root = BinNode(25)
root.left = BinNode(35)
root.right = BinNode(35)
assert(is_bst(root) == False)


root = BinNode(25)
root.left = BinNode(15)
root.right = BinNode(25)
assert(is_bst(root) == False)

root = BinNode(25)
root.left = BinNode(15)
root.right = BinNode(35)
root.left.left = BinNode(10)
root.left.right = BinNode(45)
root.right.left = BinNode(30)
root.right.right = BinNode(40)
assert(is_bst(root) == False)


