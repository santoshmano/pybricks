from linkedlist import *

def reverseGroups(head, k):
    """
    :param head: head of the list
    :param k: group size to be reversed
    :return: None1
    """

    if k < 1: return

    prev = None
    cur = head
    next = None
    index = 0
    while index < k and cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        index += 1

    if cur != None:
        head.next = reverseGroups(cur, k)

    return prev



# Test code

for j in [0, 1, 2, 3, 8, 9, 10]:
    list = LinkedList()
    for i in range(1,11):
        list.insertEnd(i)
    print("Before reversing", list)

    node = reverseGroups(list.head, j)

    print("Reversed in (", j, ") chunks")
    while node:
        print(node.val, end=" ")
        node = node.next
    print("")
