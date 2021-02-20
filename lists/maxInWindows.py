# Enter your code here. Read input from STDIN. Print output to STDOUT
class QueueNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        "insert in the tail"
        n = QueueNode(data)

        if self.head == None:
            self.head = self.tail = n
            return

        self.tail.next = n
        self.tail = n
        return

    def dequeue(self):
        "remove from the head"
        if self.head == None:
            print("Q error")
            return None

        n = self.head

        if self.head.next == None:
            self.tail = self.head = self.head.next
        else:
            self.head = self.head.next

        return n.data

def findMaxWindow(a, w):
    """
    :param a: input array of integers
    :param w: window size
    :return: array of max val in every window
    """
    max = [0] * (len(a)-w+1)
    maxPointer = 0
    maxCount = 0
    q = Queue()

    for i in range(0, w):
        if a[i] > max[maxPointer]:
            max[maxPointer] = a[i]
        elif a[i] == max[maxPointer]:
            maxCount += 1

        if w>1:
            q.enqueue(a[i])
    maxPointer += 1

    for i in range(w, len(a)):
        if w>1:
            a0 = q.dequeue()
            if a0 == max[maxPointer-1]:
                maxCount -= 1

        if a[i] > max[maxPointer-1]:
            maxCount = 0
            max[maxPointer] = a[i]
        elif a[i] == max[maxPointer-1]:
            max[maxPointer] = a[i]
            maxCount += 1
        else:
            max[maxPointer] = max[maxPointer-1]

        q.enqueue(a[i])
        maxPointer += 1

    return max

print(findMaxWindow([0,3,1,4,2,1,6,6], 2))

print(findMaxWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
#3,3,5,5,6,7

print(findMaxWindow([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
#3 3 4 5 5 5 6

print(findMaxWindow([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4))
#10 10 10 15 15 90 90

