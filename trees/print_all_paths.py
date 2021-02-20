class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_all_paths(root, path):
    if root == None:
        return

    path.append(root.val)
    print_all_paths(root.left, path)
    print_all_paths(root.right, path)

    if root.left is None and root.right is None:
        print(path)

    path.pop()

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
print("Printing all paths")
print_all_paths(root, path)

