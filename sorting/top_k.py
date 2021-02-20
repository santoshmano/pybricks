import sys
sys.path.append('../')
import MinHeap

def top_k_minheap(stream, k):
    min_heap = []
    for i in range(0, k):
        min_heap.append(stream[i]) 
    MinHeap.heapify(min_heap)

    while i < len(stream):
        if stream[i] > MinHeap.min(min_heap):
            MinHeap.delete_min(min_heap)
            MinHeap.insert(min_heap, stream[i])
        i += 1 

    return min_heap

def top_k_bubblesort(arr, k):
    for i in range(0, k):
        for n in range(len(arr)-1, i, -1):
            if arr[n-1] < arr[n]:
                arr[n-1], arr[n] = arr[n], arr[n-1]

    return [arr[x] for x in range(0, k)]

def top_k(arr, k):
    #return top_k_bubblesort(arr, k) 
    return top_k_minheap(arr,k)
if __name__ == '__main__':
    
    arr = [5, 2, -1, 3, 5, 0, -2, 9, 12, 11, 4, 1, 4, 111]
    topk = top_k(arr, 5) 
    print(topk)

    topk = top_k(arr, 1) 
    print(topk)

    topk = top_k(arr, 10) 
    print(topk)

    topk = top_k(arr, 4) 
    print(topk)
