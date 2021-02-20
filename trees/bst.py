
class BNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_print(root):

    if root == None:
        return

    inorder_print(root.left)
    print(root.val, end=" ")
    inorder_print(root.right)


# return: T/F
def is_bst1(root):
    if root == None:
        return True

    if root.left:
        if root.left.val >= root.val: return False

    if root.right:
        if root.right.val < root.val: return False

    if is_bst(root.left) == False:
        return False

    if is_bst(root.right) == False:
        return False

    return True

def is_bst(root, min, max):

    if root == None:
        return True

    if root.val < min or root.val >= max:
        return False

    if not is_bst(root.left, min, root.val):
        return False

    if not is_bst(root.right, root.val, max):
        return False

    return True


def bst_insert(root, val):

    if root == None:
        return Node(val)

    if val <= root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)

    return root

def bst_lookup(root, val):

    return None

def bst_delete(root, val):

    return

def bst_successor(root):

    return None

def bst_predecessor(root):

    return None

def bst_min(root):

    return None

def bst_max(root):

    return None


#root = Node(25)
root = None

root = bst_insert(root, 25)
root = bst_insert(root, 15)
root = bst_insert(root, 35)
root = bst_insert(root, 10)
root = bst_insert(root, 20)
root = bst_insert(root, 30)

inorder_print(root)
#print("is bst?", is_bst(root))

root = Node(6)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(8)
root.right = Node(8)
inorder_print(root)
#print("is bst?", is_bst(root))
root = None
inorder_print(root)

#bool = is_bst(root)
#print("is bst?", bool)

root = BNode(25)
root.left = BNode(15)
root.right = BNode(35)
root.left.left = BNode(10)
root.left.right = BNode(30)
print(is_bst(root, float('-inf'), float('inf')))

