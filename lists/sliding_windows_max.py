class QueueNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MaxQueue:
    def __init__(self, head=None, tail=None, len=0):
        self.head = head
        self.tail = tail
        self.len = len

    def is_empty(self):
        return self.head == None

    def length(self):
        return self.len

    def enqueue_head(self, val):
        n = QueueNode(val)
        if self.head == None:
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
        self.len += 1
        return

    def enqueue_tail(self, val):
        n = QueueNode(val)
        if self.tail == None:
            self.head = self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.len += 1
        return

    def dequeue_head(self):
        if self.is_empty():
            return None

        n = self.head
        if self.head.next == None:
            self.head = self.head.next
            self.tail = None
        else:
            self.head = self.head.next
        self.len -= 1

        return n

    def dequeue_tail(self):
        if self.is_empty():
            return None

        n = self.tail
        if self.tail.prev == None:
            self.tail = self.tail.prev
            self.head = None
        else:
            self.tail = self.tail.prev
        self.len -= 1
        return n

    def peek_tail(self):
        if self.is_empty():
            return None
        else:
            return self.tail.val

    def peek_head(self):
        if self.is_empty():
            return None
        else:
            return self.head.val

def sliding_window_max(input, win_size):

    max_windows = []
    q = MaxQueue()

    for i in range(0, win_size):
        while not q.is_empty() and input[q.peek_tail()] < input[i]:
            q.dequeue_tail()
        q.enqueue_tail(i)

    max_windows.append(input[q.peek_head()])

    for i in range(win_size, len(input)):

        while q.peek_head() < (i-win_size+1):
            q.dequeue_head()

        while not q.is_empty() and input[q.peek_tail()] < input[i]:
            q.dequeue_tail()

        q.enqueue_tail(i)
        max_windows.append(input[q.peek_head()])

    return max_windows



print(sliding_window_max([0,3,1,4,2,1,6,6], 2))
# 3, 3, 4, 4, 2, 6, 6

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
#3,3,5,5,6,7

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 2))
# 3 3 -1 5 5 6 7

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 4))
# 3 3 5 5 6 7

print(sliding_window_max([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
#3 3 4 5 5 5 6

print(sliding_window_max([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4))
#10 10 10 15 15 90 90

print(sliding_window_max([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 3))
# 10 10 10 9 15 15 90 90
