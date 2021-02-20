class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root == None:
        return
    inorder_traversal(root.left)
    print(root.val, end=' ')
    inorder_traversal(root.right)

# return: a cloned tree
def clone_tree(root):
    if root == None:
        return None

    clone = Node(root.val)
    clone.left = clone_tree(root.left)
    clone.right = clone_tree(root.right)

    return clone


def create_bin_tree1():
    root = Node(25)

    root.left = Node(15)
    root.left.left = Node(10)
    root.left.right = Node(20)

    root.right = Node(35)
    root.right.left = Node(30)
    root.right.right = Node(40)

    return root

root = create_bin_tree1()
path = []

inorder_traversal(root)
print(":tree inorder")
clone_root = clone_tree(root)
inorder_traversal(clone_root)
print(":cloned tree inorder")