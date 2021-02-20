
#1   2   3
#  1   2   3


class Node:
    def __init__(self, val, next=None, arbit=None):
        self.val = val
        self.next = next
        self.arbit = arbit

def clone(head):
    if head == None: return

    temp = head
    while temp != None:
        n = Node(temp.val, temp.next, temp.arbit)
        temp.next = n
        temp = n.next

    chead = head.next
    temp = head

    while temp!= None:
        ctemp = temp.next
        ctemp.arbit = temp.arbit.next
        temp.next = ctemp.next

        temp = ctemp.next

    return chead





n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)
n1.arbit = n3
n2.arbit = n1
n3.arbit = n2

head2 = clone(n1)

print(n1.val, n1.next, n1.arbit)
print(n2.val, n2.next, n2.arbit)
print(n3.val, n3.next, n3.arbit)

for temp in n1, head2:
    while temp != None:
        print(temp.val,"(", temp.arbit.val, ")", end=" ")
        temp = temp.next
    print("\n")

