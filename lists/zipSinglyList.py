from linkedlist import *


def splitMiddle(head):
    prev = None
    slow = fast = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev:
        prev.next = None

    return slow

def reverse(head):
    prev = None
    cur = head

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev

def merge(head, mid):
    while head and mid:

        temp = head.next
        head.next = mid
        temp2 = mid.next
        mid.next = temp

        head = temp
        mid = temp2

def zipList(head):
    mid = splitMiddle(head)
    mid = reverse(mid)

    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

    temp = mid

    merge(head, mid)
    print(head.val)
    return

list = LinkedList()
for i in range(1,10):
    list.insertEnd(i)

print("List - ",   list)
zipList(list.head)
print("Zipped List - ",   list)


list = LinkedList()
for i in [5, 8, 34, 66, 43, 88888]:
    list.insertEnd(i)

print("List - ",   list)
zipList(list.head)
print("Zipped List - ",   list)