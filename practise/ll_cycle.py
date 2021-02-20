class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def has_cycle(head):
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = (fast.next).next

        if slow == fast:
            len = 1
            fast = fast.next
            while fast != slow:
                len += 1
                fast = fast.next
            return len

    return 0

def get_cycle(head):
    if head == None:
        return None, 0

    len = has_cycle(head)

    if len > 0:
        fast = Node(-1, head)
        for _ in range(0,len):
            fast = fast.next

        slow = Node(-1, head)
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow, len
    else:
        return None, 0

def main():
    start = Node(2)
    start.next = Node(1, start)
    head = Node(5, Node(4, Node(3, start)))
    assert(has_cycle(head) == 2)
    assert((start, 2) == get_cycle(head))

    start = Node(2)
    start.next = start
    head = Node(5, Node(4, Node(3, start)))
    assert(has_cycle(head) == 1)
    assert((start, 1) == get_cycle(head))

    start = Node(2)
    start.next = Node(1, Node(0, start))
    head = Node(6, Node(5, Node(4, Node(3, start))))
    assert(has_cycle(head) == 3)
    assert((start, 3) == get_cycle(head))

    head = Node(2)
    head.next = head
    assert(has_cycle(head) == 1)
    assert((head, 1) == get_cycle(head))

    head = None
    assert(has_cycle(head) == 0)
    assert((None, 0) == get_cycle(head))

if __name__ == "__main__":
    main()
