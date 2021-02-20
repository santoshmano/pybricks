
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_lca(root, n1, n2):
    if root == None:
        return None

    if root.val == n1 or root.val == n2:
        return root

    left = find_lca(root.left, n1, n2)
    right = find_lca(root.right, n1, n2)

    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right
    else:
        return None

if __name__ == "__main__":
    root = Node(25)
    root.left = Node(15)
    root.right = Node(35)
    root.left.left = Node(10)
    root.left.right = Node(20)
    root.right.left = Node(30)
    root.right.right = Node(40)

    print("LCA of (15, 40)", find_lca(root, 15, 40).val)
    print("LCA of (15, 25)", find_lca(root, 15, 25).val)
    print("LCA of (10, 20)", find_lca(root, 10, 20).val)
    print("LCA of (15, 30)", find_lca(root, 15, 30).val)
    print("LCA of (10, 40)", find_lca(root, 10, 40).val)
    print("LCA of (30, 40)", find_lca(root, 30, 40).val)

