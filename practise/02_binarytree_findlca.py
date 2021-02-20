# Given a binary tree and two nodes, find the lca

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def find_lca(root, n1, n2):
	if root == None:
		return root

	if root == n1 or root == n2:
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


def find_lca_bst(root, n1, n2):
	if root == None:
		return None

	if n1.val < root.val and n2.val < root.val:
		return find_lca_bst(root.left, n1, n2)
	
	if n1.val > root.val and n2.val > root.val:
		return find_lca_bst(root.right, n1, n2)

	return root\

if __name__ == '__main__':
	root = Node(25)
	l1 = Node(15)
	r1 = Node(35)
	l2 = Node(10)
	r2 = Node(20)
	l3 = Node(30)
	r3 = Node(40)
	r4 = Node(12)

	root.left = l1
	root.right = r1
	l1.left = l2
	l1.right = r2
	r1.left = l3
	r1.right = r3
	l2.right = r4

	lca = find_lca(root, None, None)
	
	if lca:
		print(lca.val)
	else:
		print("not found")

	lca = find_lca(root, l2, r3)
	
	if lca:
		print(lca.val)
	else:
		print("not found")

	lca = find_lca(root, None, None)
	
	if lca:
		print(lca.val)
	else:
		print("not found")

	lca = find_lca(root, r1, r3)
	
	if lca:
		print(lca.val)
	else:
		print("not found")

	lca = find_lca(root, l3, r4)
	
	if lca:
		print(lca.val)
	else:
		print("not found")

	lca = find_lca(root, l2, r2)
	
	if lca:
		print(lca.val)
	else:
		print("not found")
