import maxheap

def heapsort(arr):
    maxheap.heapify(arr)

    for end in range(len(arr)-1, -1, -1):
        maxheap._swap(arr, 0, end)
        maxheap._siftdown(arr, 0, end-1)

if __name__ == "__main__":
    arr = [-1, 3, 4, 1, 9, 0, 3, 2]
    print(arr)
    heapsort(arr)
    print(arr)
