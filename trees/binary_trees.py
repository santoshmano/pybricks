
class BNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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



if __name__ == "__main__":

    root = BNode(25)
    root.left = BNode(15)
    root.right = BNode(15)
    print(is_bst(root, float('-inf'), float('inf')))

    root = None
    print(is_bst(root, float('-inf'), float('inf')))

    root = BNode(25)
    root.left = BNode(15)
    root.right = BNode(35)
    print(is_bst(root, float('-inf'), float('inf')))

    root.left = BNode(35)
    root.right = BNode(35)
    print(is_bst(root, float('-inf'), float('inf')))

    root.left = BNode(15)
    root.right = BNode(15)
    print(is_bst(root, float('-inf'), float('inf')))


    root.left = BNode(15)
    root.right = BNode(35)
    root.left.left = BNode(10)
    root.left.right = BNode(30)
    print(is_bst(root, float('-inf'), float('inf')))

    root.left = BNode(15)
    root.right = BNode(35)
    root.left.left = BNode(10)
    root.left.right = BNode(20)
    print(is_bst(root, float('-inf'), float('inf')))
