class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next
    return tail

class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, val):
        return self.data.append(val)

    def pop(self):
        if self.isEmpty():
            return -1

        return self.data.pop()


class Queue:

    def __init__(self):
        self.mainStk = Stack()
        self.auxStk = Stack()

    def enqueue(self, val):

        while self.mainStk.isEmpty() == False:
            self.auxStk.push(self.mainStk.pop())

        self.mainStk.push(val)

        while self.auxStk.isEmpty() == False:
            self.mainStk.push(self.auxStk.pop())

        return

    def dequeue(self):
        if self.mainStk.isEmpty():
            return -1
        else:
            return self.mainStk.pop()


#4 1 2 -1 -1



def  ImplementQueue(operationsList):

    temp = operationsList
    q = Queue()

    output_head = None
    output_tail = None
    first = 1

    print("Queue ops")

    while temp != None:
        if temp.val == -1:
            val = q.dequeue()
            print("\ndeque - ", val, end=" ")
            output_tail = _insert_node_into_singlylinkedlist(output_head, output_tail, val)
            if first:
                output_head = output_tail
                first = 0

        else:
            q.enqueue(temp.val)
            print("\nenqueue - ", temp.val, end=" ")

        temp = temp.next

    print(output_head, output_tail)
    return output_head


n1 = LinkedListNode(4)
n2 = LinkedListNode(1)
n3 = LinkedListNode(2)
n4 = LinkedListNode(-1)
n5 = LinkedListNode(-1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


head = ImplementQueue(n1)

temp = head
print("\nPrinting output")
while temp != None:
    print(temp.val, end=" ")
    temp = temp.next


