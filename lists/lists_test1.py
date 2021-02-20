
def  LinkedListIntersection():

    int = -1

    return int


Implement
a
queue
using
exactly
two
stacks.

e.g:
1.
Q.enqueue(1), Q.enqueue(2)
Q.dequeue()
Q.dequeue()
should
return 1, 2 in that
order.
2.
Q.enqueue(1), Q.dequeue(), Q.dequeue()
should
return 1
followed
by
throwing “-1” (signifying
an
exception)

Test
case
Input:
A
singly
linked
list
of
enqueue / dequeue
operations.Positive
values
are
enqueues and negative
values
are
dequeues.
e.g.
1
2
-1
-1

means
Q.enqueue(1), Q.enqueue(2), Q.dequeue and Q.dequeue

Test - case
Output:
A
singly
linked
list
of
dequeued
values.e.g.
for the above example, you should form a linked list of two values, 1 and 2.
In
the
case
where
there is nothing
left
to
dequeue, and you
still
see
a
dequeue
operation in the
test
input, feel
free
to
append
a
node
with -1 to your output linked list.

Feel
free
to:
1.
Assume
that
the
values
are
all
integers
2.
This is better
done as a
whiteboard
question.So
you
can
copy / paste
an
implementation
of
a
stack


class . It's not too difficult to write one quickly with push/pop, but if you want to save time, you can.

