
class BstIterator:
    def __init__(self, root):
        self.stack = list()
        self.push_all_left(root)

    def hasNext(self):
        return True if len(self.stack) > 0 else False

    def next(self):
        tmpNode = self.stack.pop()
        self.push_all_left(tmpNode.right)
        return tmpNode.val

    def push_all_left(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

class BNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    root = BNode(25)
    root.left = BNode(15)
    root.right = BNode(35)
    root.left.left = BNode(10)
    root.left.right = BNode(20)

    root_iter = BstIterator(root)

    while root_iter.hasNext(): print(root_iter.next())
