
from operator import itemgetter

"""
Merge Overlapping Intervals

example - for this input: {{1,3}, {2,4}, {5,7}, {6,8}}.
The intervals {1,3} and {2,4} overlap with each other,
so they should be merged and become {1, 4}. Similarly
{5, 7} and {6, 8} should be merged and become {5, 8}.


input - an list of tuples
output - a list of non-overlapping tuples
"""

# inefficient O(n**2) solution
# check set X with all the other sets
#   - if the two merge then set it to X
#   - remove the other merged set
#   - remove it by maintaining a map of removed items.
# Do the above for all sets in the list.
def merge_overlap_1(a):
    # create a copy
    b = [[None for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        b[i][0] = a[i][0]
        b[i][1] = a[i][1]

    validity_map = [1 for _ in range(len(b))]

    for i in range(0, len(b)):
        if not validity_map[i]:
            continue
        for j in range(i+1, len(b)):
            if not validity_map[j]:
                continue

            if b[i][1] >= b[j][1]:
                b[i][0] = min(b[i][0], b[j][0])
                b[i][1] = max(b[i][1], b[j][1])
                validity_map[j] = 0

    c = []
    for i in range(len(validity_map)):
        if validity_map[i]:
            c.append(b[i])

    return c

# O(n) solution
# sort the list of elements based on first item in the tuple
# merge elements in a linear fashion
def merge_overlap(a):
    #a.sort(key=lambda x: x[0])
    a.sort(key=itemgetter(0))

    i = 0
    j = i+1
    while i < len(a) and j < len(a):
        if a[i][1] >= a[j][0]:
            a[i][1] = max(a[i][1], a[j][1])
            a[j] = None
            j += 1
            continue
        i = j
        j = i+1

    a = [x for x in a if x is not None]
    return a


a = [[2,4], [6,8], [5,7], [1,3]]
print(a)
print(merge_overlap_1(a))
a = [[2,4], [6,8], [5,7], [1,3]]
print(merge_overlap(a))
