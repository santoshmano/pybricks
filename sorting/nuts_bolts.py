"""
nuts  = 3, 5, 4, 1, 2

bolts = 4, 3, 1, 2, 5

no duplicates
compare with 1 nut and bolt only, ie cannot compare among
    nuts or bolts themselves. 

- pick a nut, and partition the bolts based on the nut. Automatically the matching bolt will fall in the right location. 
- pick the bolt, and partition the nuts accordingly. 
-- do the above smaller partitions
"""

def _match_nb(nuts, bolts, start, end):
    if start < end:
        pivotb = end
        pivotn = partition(nuts, start, end, bolts[pivotb])
        pivotb = partition(bolts, start, end, nuts[pivotn])
        assert(pivotn == pivotn)

        _match_nb(nuts, bolts, start, pivotb-1)
        _match_nb(nuts, bolts, pivotb+1, end)

def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def partition(arr, start, end, pivotval):
    left = start
    right = end
 
    while left <= right:
        if arr[left] == pivotval:
            swap(arr, left, end)
            right -= 1
        elif arr[left] < pivotval:
            left += 1
        elif arr[right] > pivotval:
            right -= 1
        else:
            swap(arr, left, right)

    swap(arr, end, left)
    return left

def match_nb(nuts, bolts):
    _match_nb(nuts, bolts, 0, len(bolts)-1)

if __name__ == '__main__':
    nuts = [3, 5, 4, 1, 2]
    bolts = [4, 3, 1, 2, 5]

    match_nb(nuts, bolts)
    print(nuts)
    print(bolts)
