
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def alternative_split(head):

    h1 = temp_h1 = Node(0)
    h2 = temp_h2 = Node(0)

    while head:
        h1.next = head
        h2.next = head.next

        h1 = h1.next
        h2 = h2.next

        if head.next:
            head = head.next.next

    h1.next = None
    h2.next = None
    h1 = temp_h1.next
    h2 = temp_h2.next

    return h1, h2


head = Node(5)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(5)

h1, h2 = alternative_split(head)

while h1:
    print("{},".format(h1.val), end=" ")
    h1 = h1.next
print()
while h2:
    print("{},".format(h2.val), end=" ")
    h2 = h2.next
