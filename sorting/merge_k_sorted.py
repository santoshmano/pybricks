"""
Merge k sorted arrays
duplicates present
"""
import sys
sys.path.append('../')
import MinHeap

def _merge_sorted_arrays(arrays, k):
    mheap = []
    arrayi = [0 for i in range(0,k)]

    for i in range(0, k):
        if arrays[i] == []:
            continue
        mheap.append(arrays[i][0])
        arrayi[i] += 1

    MinHeap.heapify(mheap)

    result = []
    while mheap:
        min, i = MinHeap.delete_min(mheap)
        result += min
        MinHeap.insert(mheap, (arrays[i][arrayi[i]], array[i]))

    return mheap

def merge_sorted_arrays(arrays):
    if (len(arrays) == 0):
        return
    _merge_sorted_arrays(arrays, len(arrays))

if __name__ == '__main__':
    arrays = [[1, 3, 5, 7],
              [2, 4, 6, 8], 
              [0, 9, 10, 11]]

    merge_sorted_arrays(arrays)
