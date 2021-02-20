"""
Merge sort a linked list
O(nlog(n)) time complexity.
O(1) space.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def list_to_str(head):
    temp = head
    list = []
    while temp:
       list.append(temp.val)
       temp = temp.next

    return ",".join(map(str, list))

def list_length(head):
    temp = head
    len = 0
    while temp:
        len += 1
        temp = temp.next

    return len

def _merge_lists(h1, h2):
    head = temp_head = Node(0)

    while h1 and h2:
        if h1.val < h2.val:
            head.next = h1
            h1 = h1.next
        else:
            head.next = h2
            h2 = h2.next
        head = head.next

    if h1:
        head.next = h1
    elif h2:
        head.next = h2

    head = temp_head.next
    del temp_head

    return head

"""
examples:

List        len     mid     h1      h2
3 1         2       1       3       1
3 5 1 3     4       2       3       1
8 1 4 1 9   5       2
"""
def _mergesort_list(head, len):

    if len == 0 or len == 1:
        return head

    mid = len // 2
    left = right = head

    # get the middle list pointer/reference
    prev = None
    for i in range(mid):
        prev = right
        right = right.next

    #split it into two lists
    if prev:
        prev.next = None


    h1 = _mergesort_list(left, mid)
    h2 = _mergesort_list(right, len - mid)
    head = _merge_lists(h1, h2)

    return head

def mergesort_list(head):
    """
    :param head: list to be sorted
    :return: head of the sorted list
    """
    len = list_length(head)
    return _mergesort_list(head, len)



head = Node(5)
head.next = Node(1)
head.next.next = Node(2)

head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(5)

print("Original list:", list_to_str(head))
head = mergesort_list(head)
print("Sorted list:", list_to_str(head))
