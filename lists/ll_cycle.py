
# Problem - detect cycle in a loop
# Variation - how to find out the number of nodes in the loop
# Variation - how do you find beginning of the loop
#
# different problem - simlar to above variation:Find nth node from the end

class Node:
 def __init__(self, data, next=None):
     self.data = data
     self.next = next


def hasCycle(head):
    fast = head
    slow = head

    while (fast and fast.next):
        slow = slow.next
        fast = (fast.next).next

        if slow == fast:
            return True

    return False
