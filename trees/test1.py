class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_bst(arr, start_index, end_index):

    if start_index > end_index:
        return None
    elif start_index == end_index:
        mid = start_index
    else:
        mid = (end_index-start_index)//2 + start_index

    root = Node(arr[mid])
    print(start_index, end_index, mid, arr[mid])

    root.left = create_bst(arr, start_index, mid-1)
    root.right = create_bst(arr, mid+1, end_index)

    return root


def levelorder_print(root):

    if root == None:
        return
    q = []
    q.insert(0, root)

    while True:
        count = len(q)
        if count == 0:
            break

        while count:
            n = q.pop()
            count -= 1

            print(n.val, end=" ")

            if n.left:
                q.insert(0, n.left)
            if n.right:
                q.insert(0, n.right)
        print("")

def createBalancedBST(iArray):
    print(iArray, len(iArray))

    start = 0
    end = len(iArray)-1
    root = create_bst(iArray, start, end)
    levelorder_print(root)

createBalancedBST([10, 15, 20, 25, 30, 35, 40, 45])
#createBalancedBST([10, 15, 20, 25, 30, 35, 40])
#createBalancedBST([10, 15, 20, 25])

"""
root1 = Node(25)
root1.left = Node(15)
root1.right = Node(35)
root1.left.left = Node(10)
root1.left.right = Node(20)
root1.right.left = Node(30)
root1.right.right = Node(40)

levelorder_print(root1)

root1 = Node(25)
levelorder_print(root1)

root1 = None
levelorder_print(root1)
"""
