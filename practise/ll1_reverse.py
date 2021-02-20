
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

"""
def reverse_list(head):
    prev = None
    cur = head

    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev

def print_list(head):
    printlist = []
    while(head):
        printlist.append(head.val)
        head = head.next
    print(printlist)


head = Node(0)
print_list(head)
head = reverse_list(head)
print_list(head)

head = None
print_list(head)
head = reverse_list(head)
print_list(head)

head = Node(5)
head.next = Node(6)
head.next.next = Node(7)
head.next.next.next = Node(8)
head.next.next.next.next = Node(9)

print_list(head)
head = reverse_list(head)
print_list(head)

head = Node(0)
head.next = Node(0)
head.next.next = Node(-1)
head.next.next.next = Node("ssd")
head.next.next.next.next = Node(9.5)

print_list(head)
head = reverse_list(head)
print_list(head)


