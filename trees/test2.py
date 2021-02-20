
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        # idea
def kth_smallest_bst(root1, root2, k):

    if root1 == None:
        return root2

    node = None

    if k <= 0:
        root2=root2.left

    node = kth_smallest_bst(root1.left,root2, k-1)

    if k <= 0:
        root2=root2.right

    node = kth_smallest_bst(root1.left,root2, k-1)

    return node


root1 = Node(25)
root1.left = Node(15)
root1.right = Node(35)
root1.left.left = Node(10)
root1.left.right = Node(20)
root1.right.left = Node(30)
root1.right.right = Node(40)

node1 = kth_smallest_bst(root1, root1, 3)

if node1:
    print(node.val)
