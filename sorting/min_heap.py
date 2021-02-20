# Min Heap implementation
def swap(h, i, j):
    h[i], h[j] = h[j], h[i]

def _min_heap_sift_up(h, k):
    while k//2 >= 0:
        if h[k] < h[k//2]:
            swap(h, k, k//2)
            k = k//2
        else:
            break

def _min_heap_sift_down(h, k):
    last = len(h)-1

    while (2*k+1) < last:
        child = 2*k+1

        if child < last and h[child+1] < h[child]:
            child = child+1

        if h[child] > h[k]:
            break

        swap(h, child, k)
        k = child

def min_heap_heapify(h):
    for k in range(len(h)//2, 0, -1):
        _min_heap_sift_up(h, k)

def min_heap_insert(h, key):
    h.append(key)
    k = len(h)-1
    print("appended", k, key, h)

    _min_heap_sift_up(h, k)
    print("appended", k, key, h)

def min_heap_getmin(h):
    if len(h) == 0:
        return None

    return h[0]

def min_heap_deletemin(h):
    if len(h) == 0:
        return None

    last = len(h)-1
    first = 0

    min = h[0]
    swap(h, first, last)
    h.pop()
    print("deleted", min, h)
    _min_heap_sift_down(h, 0)
    print("deleted", min, h)

    return min

# Min heap usage
#a = ['s', 'o', 'r', 't', 'e', 'x', 'a', 'm', 'p', 'l', 'e']
a = [1, -1, 0, 3, 9, 8, 3]
print(a)
min_heap_heapify(a)
print("Heapified", a)
min_heap_insert(a, 2)
print(a)
min_heap_insert(a, 0)
print(a)
min_heap_insert(a, -1)

print(min_heap_getmin(a))
print(a)
min_heap_deletemin(a)
print(a)
min_heap_deletemin(a)
print(a)
min_heap_deletemin(a)
print(a)
