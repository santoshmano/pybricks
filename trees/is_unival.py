class BNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def _unival(root):
    if root == None:
        return (False, 0)

    if root.left == None and root.right == None:
        return (True, 1)

    l_count, r_count = 0, 0

    if root.left:
        (l_is_unival, l_count) = _unival(root.left)

    if root.right:
        (r_is_unival, r_count) = _unival(root.right)

    root_count = l_count + r_count
    root_is_unival = False
    if root.left and not root.right:
        if l_is_unival and root.left.val == root.val:
            root_is_unival = True
            root_count += 1
    elif root.right and not root.left:
        if r_is_unival and root.right.val == root.val:
            root_is_unival = True
            root_count += 1
    elif root.left and root.right:
        if l_is_unival and root.left.val == root.val and r_is_unival and root.right.val == root.val:
            root_is_unival = True
            root_count += 1

    return (root_is_unival, root_count)

def unival(root):
    (is_unival, count) = _unival(root)
    return count


root = BNode(5)
root.left = BNode(5)
root.right = BNode(6)
root.left.left = BNode(5)
root.left.right = BNode(5)

root.right.left = BNode(5)
root.right.right = BNode(5)
root.right.right.right = BNode(1)

print(unival(root))

root = BNode(5)
root.left = BNode(5)
root.right = BNode(5)
root.right.left = BNode(5)
root.right.right = BNode(5)
print(unival(root))
