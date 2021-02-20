
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left        # morphs to prev
        self.right = right      # morphs to next


def bst_to_cll(root):
    if root == None:
        return None

    ll = bst_to_cll(root.left)
    if ll:
        ll.left.right = root
        root.left = ll.left
        ll.left = root
        #TODO root.right
    else:
        ll = root
        ll.left = root

    rl = bst_to_cll(root.right)

    if rl:
        root.right = rl
        rl.left.right = ll
        ll.left = rl.left
        rl.left = root
    else:
        root.right = ll

    return ll


