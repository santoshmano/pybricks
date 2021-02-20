# Given a singly linked list, zip and unzip it. 
class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def split(head):
	prev = None
	slow = fast = head

	while fast and fast.next:
		prev = slow
		slow = slow.next
		fast = fast.next.next

	if prev:
		prev.next = None

	return slow

def reverse(head):
	prev = None
	cur = head

	while cur:
		next = cur.next
		cur.next = prev
		prev = cur
		cur = next

	return prev

def merge(head1, head2):
	while head1 and head2:
		temp1 = head1.next
		head1.next = head2
		temp2 = head2.next
		head2.next = temp1

		head1 = temp1
		head2 = temp2
	
def zip(head):
	if not head:
		return head

	head2 = split(head)
	if not head2:
		return head

	head2 = reverse(head2)
	merge(head, head2)
	return head

def printlist(head):
	temp = head	
	while head:
		print(head.val)
		head = head.next
	head = temp

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
printlist(head)
zip(head)
printlist(head)


