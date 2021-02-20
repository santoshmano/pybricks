class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
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


n = Node(5)
n.next = Node(6)
n.next.next = Node(7)
n.next.next.next = Node(8)