class DoublyLinkedQ:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def enqueue_head(self, n):
        if self.head == None:
            self.head = self.tail = n
        else:
            self.head.prev = n
            n.next = self.head
            n.prev = None
            self.head = n

        self.len += 1
        return

    def unlink(self, n):
        if n == self.head and n == self.tail:
            # only 1 element in q
            self.head = self.tail = None
        elif n == self.head:
            self.head = self.head.next
        elif n == self.tail:
            self.tail = self.tail.prev
        elif self.head == None:
            pass
        else:
            n.prev.next = n.next
            n.next.prev = n.prev

        n.next = n.prev = None

        self.len -= 1
        return

    def get_oldest(self):
        return self.tail

    def get_latest(self):
        return self.head
