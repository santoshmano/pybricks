# Find middle of a singly linked list
# Constraints
# - Do it in one pass
# - If N is even, return second of middle 2 elements

#!/bin/python3

import sys
import os

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


def findMiddleNode(head):
    '''
    :param head: head node of the singlyLL
    :return: node_value of the middle node
    '''

    fast = slow = head
    while (fast and fast.next):
        slow = slow.next
        fast = (fast.next).next

    if slow:
        return slow.val
    else:
        return None


_pList = None
_pList_tail = None
_pList_size = 0
print("Enter the size of the list")
_pList_size = int(input())
_pList_i = 0
print("Enter the elements of the list")
while _pList_i < _pList_size:
    _pList_item = int(input());
    if _pList_i == 0:
        _pList = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item)
        _pList_tail = _pList
    else:
        _pList_tail = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item)
    _pList_i += 1

res = findMiddleNode(_pList);
print("Middle of the list is ", res)
