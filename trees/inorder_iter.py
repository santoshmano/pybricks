class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_iter(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root: return

    processed = set()
    stk = list()
    stk.append(root)
    result = []

    while stk:
        node = stk.pop()
        if node.right:
            stk.append(node.right)

        if not node.left or node in processed:
            result.append(node.val)
        else:
            stk.append(node)
            processed.add(node)
            node = node.left

    return result


def postorder_iter(root):

    if not root:
        return

    stk = list()
    proc = set()
    result = list()

    stk.append(root)

    while stk:
        node = stk.pop()

        if node in proc:
            result.append(node.val)
        else:
            stk.append(node)
            proc.add(node)
            if node.right: stk.append(node.right)
            if node.left: stk.append(node.left)

    return result


root1 = Node(25, Node(15, Node(10), Node(20)))
root2 = Node(25, Node(15, Node(10), Node(20)), Node(35, Node(30), Node(40)))

print(root2.val)
for root in root1, root2:
    #print(inorder_iter(root))
    print(postorder_iter(root))