def level_order_print(root):
    q = []
    if root: q.append(root)

    while True:
        count = len(q)
        if count == 0:
            break

        while count:
            node = q.pop(0)
            count -= 1
            print(node.val, end=' ')
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        print()

def bst_to_sorted_arr(root, arr):
    if root == None:
        return

    bst_to_sorted_arr(root.left, arr)
    arr.append(root.val)
    bst_to_sorted_arr(root.right, arr)

def merge_arrays(a1, a2, a):

    i1, i2 = 0, 0

    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] <= a2[i2]:
            a.append(a1[i1])
            i1 += 1
        else:
            a.append(a2[i2])
            i2 += 1

    if i1 == len(a1):
        while i2 < len(a2):
            a.append(a2[i2])
            i2 += 1
    elif i2 == len(a2):
        while i1 < len(a1) :
            a.append(a1[i1])
            i1 += 1

    return

def _array_to_bst(arr, start, end):

    if start == end:
        return None

    mid = (start+end)//2

    root = Node(arr[mid])
    root.left = _array_to_bst(arr, start, mid)
    root.right = _array_to_bst(arr, mid+1, end)

    return root


def array_to_bst(arr):
    return _array_to_bst(arr, 0, len(arr))

def merge_trees(r1, r2):
    # convert bst to sorted array
    a1, a2 = [], []
    bst_to_sorted_arr(r1, a1)
    bst_to_sorted_arr(r2, a2)
    print(a1)
    print(a2)

    # merge sorted arrays
    a = []
    merge_arrays(a1, a2, a)
    print(a)

    # convert array to bst tree
    root = array_to_bst(a)

    return root


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val, self.left, self.right = val, left, right

r1 = Node(25)
r1.left = Node(15)
r1.right = Node(35)
r1.left.left = Node(10)
r1.left.right = Node(20)

r2 = Node(26)
r2.left = Node(16)
r2.right = Node(36)
r2.left.left = Node(11)
r2.left.right = Node(21)
r2.right.left = Node(31)
r2.right.right = Node(41)

root = merge_trees(r1, r2)
level_order_print(root)

