from linkedlist import *

def swapTwoNodes(head, prev1, node1, prev2, node2):

    #print(node1.val, node2.val, prev1, prev2)
    #if prev1: print("prev1", prev1.val)
    #if prev2: print("prev2", prev2.val)
    if prev1:
        prev1.next = node2

    node2Next = node2.next

    if node1.next != node2:
        node2.next = node1.next
        if prev2:
            prev2.next = node1
    else:
        node2.next = node1

    node1.next = node2Next

    #print(node1.val, node2.val, prev1, prev2)
    #if prev1: print("prev1", prev1.val)
    #if prev2: print("prev2", prev2.val)

    if not prev1:
        return node2
    elif not prev2:
        return node1
    else:
        return head


def swapNodes(head, k):

    if head == None or head.next == None:
        return

    node1 = node2 = head
    prev1 = prev2 = None

    # get node1
    index = 1
    while index < k:
        prev1 = node1
        node1 = node1.next
        index += 1

    temp = node1

    # get node2
    while temp.next != None:
        temp = temp.next
        prev2 = node2
        node2 = node2.next

    head = swapTwoNodes(head, prev1, node1, prev2, node2)

    return head



list = LinkedList()
for i in range(1,11):
    list.insertEnd(i)

for i in range(1,11):
    print("List before and after swap of k(",i,")th nodes:\n", list)
    list.head = swapNodes(list.head, i)
    print(list)
    list.head = swapNodes(list.head, i)
