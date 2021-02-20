class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root, result):
    if root == None: return

    postorder_traversal(root.left, result)
    postorder_traversal(root.right, result)

    result.append(root.val)


def postorder_iterative_traversal(root, result):
    if root == None: return

    node = root
    stk = []
    visited = set()

    while node or stk:
        if node:
            stk.append(node)
            node = node.left
        else:
            node = stk.pop()
            if node.right and node.right not in visited:
                stk.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.val)
                node = None


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

result = []
postorder_traversal(root, result)
print("Post order recursive", result)

del result
result = []
postorder_iterative_traversal(root, result)
print("Post order Iterative:", result)

