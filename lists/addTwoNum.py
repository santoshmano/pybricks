"""
Add two numbers given via a linked list

Example
12 + 35 = 47

Linked List representation
n1->2->1->None
n2->5->3->None
sum->7->4->None

Algorithm

Do this until n1 and n2 is not NULL
    n3 = (n1+n2)%10 + previous_remainder.
    remainder = (n1+n2)//10

    move n1 and n2 pointers
    create n3 nodes as we progress.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None

    def insertEnd(self, val):
        n = Node(val)
        if self.head == None:
            self.head = self.tail = n
        else:
            self.tail.next = n
        self.tail = n

    def __str__(self):
        temp = self.head
        s = "-"
        while temp:
            s =  s + " " + str(temp.val)
            temp = temp.next

        return s

def add_numbers(l1, l2):

    sum = LinkedList()
    remainder = 0

    while l1 is not None or l2 is not None:
        if l1:
            num1 = l1.val
        else:
            num1 = 0

        if l2:
            num2 = l2.val
        else:
            num2 = 0

        num3 = (num1+num2) % 10 + remainder
        remainder = (num1+num2) // 10

        print(num1, num2, num3, remainder)
        if l1: l1 = l1.next
        if l2: l2 = l2.next

        sum.insertEnd(num3)

    if remainder:
        sum.insertEnd(remainder)

    return sum.head


l1 = LinkedList()
l2 = LinkedList()

l1.insertEnd(2)
l1.insertEnd(1)

l2.insertEnd(3)
l2.insertEnd(2)

sum = add_numbers(l1.head,l2.head)
print(sum)

l1 = LinkedList()
l2 = LinkedList()
l1.insertEnd(3)
l1.insertEnd(5)
l1.insertEnd(6)

l2.insertEnd(9)
l2.insertEnd(9)
l2.insertEnd(8)

lsum = add_numbers(l1.head,l2.head)
print(lsum)

l1 = LinkedList()
l2 = LinkedList()

l1.insertEnd(9)
l2.insertEnd(3)
l2.insertEnd(2)
l2.insertEnd(1)

sum = add_numbers(l1.head,l2.head)
print(sum)
