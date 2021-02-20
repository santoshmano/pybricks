
# maxheight of a k-ary tree

MAX_CHILD = 10
class Node:
    def __init__(self, val):
        self.val = val
        self.child = []

        for i in range(0, MAX_CHILD):
            self.child.append(None)

"""



"""


def kary_max_height(root):

    if root == None:
        return 0

    height = 0

    for i in range(0,MAX_CHILD):
        height = max(height, kary_max_height(root.child[i]))

    return max_height + 1


root = Node(1)
root.child[0] = Node(13)
root.child[1] = Node(15)
root.child[2] = Node(17)


root.child[0].child[0] = Node(21)
root.child[0].child[1] = Node(22)
root.child[0].child[2] = Node(23)

root.child[0].child[0] = Node(33)


print(kary_max_height(root))

root = Node(1)
print(kary_max_height(root))


root = Node(1)
root.child[0] = Node(13)
print(kary_max_height(root))

