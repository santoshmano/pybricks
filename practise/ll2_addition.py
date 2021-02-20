class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


"""
input: two lists holding the numbers
output: one list of the sum

Reverse both the lists
while either list is not empty
    new sum = sum of l1 + l2 + remainder

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

def add_numlist(l1, l2):
    l1 = reverse_list(l1)
    l2 = reverse_list(l2)

# use dummy node

    rem = 0
    sumlist = None
    sumlist_head = None
    while l1  or l2 :
        num1, num2, sum = 0, 0, 0
        if l1:
            num1 = l1.val
            l1 = l1.next

        if l2:
            num2 = l2.val
            l2 = l2.next

        sum = (num1 + num2 + rem) % 10
        rem = (num1 + num2) // 10

        if sumlist:
            sumlist.next = Node(sum)
            sumlist = sumlist.next
        else:
            sumlist = Node(sum)
            sumlist_head = sumlist

    if rem:
        sumlist.next = Node(rem)

    return reverse_list(sumlist_head)

l1 = Node(1)
l1.next = Node(4)
l1.next.next = Node(7)

l2 = Node(8)
l2.next = Node(9)

print_list(add_numlist(l1, l2))

l1, l2 = None, None
print_list(add_numlist(l1, l2))

l1 = Node(9)
l2 = None
print_list(add_numlist(l1, l2))

l1 = Node(9)
l2 = Node(9)
print_list(add_numlist(l1, l2))
