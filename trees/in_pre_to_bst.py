class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_pre_to_bst(inorder, preorder):
    in_map = {data : index for index, data in enumerate(inorder)}
    print(in_map)
    def _in_pre_to_bst(in_s, in_e, pre_s, pre_e):

        if in_s >= in_e or pre_s >= pre_e:
            return None

        root = Node(preorder[pre_s])

        root_in_index = in_map[root.val]
        left_tree_size = root_in_index - in_s

        root.left = _in_pre_to_bst(in_s, root_in_index, pre_s+1, pre_s+1+left_tree_size)
        root.right = _in_pre_to_bst(root_in_index+1, in_e, pre_s+1+left_tree_size, pre_e )

        return root

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
                print(node.val, end = ' ')
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            print()

    level_order_print(_in_pre_to_bst(0, len(inorder), 0, len(preorder)))

root = in_pre_to_bst([10, 15, 20, 23, 25, 27, 30, 35, 40],
                     [25, 15, 10, 20, 23, 35, 30, 27, 40])

#level_order_print(root)
root = in_pre_to_bst([1, 2, 3],
                     [2, 1, 3])
#level_order_print(root)
