# min heap module
def heapify(arr):
    start = len(arr)//2
    end = len(arr)-1

    while start > -1:
        _siftdown(arr, start, end)
        start -= 1

def insert(arr, key):
    arr.append(key)
    _siftup(arr, len(arr)-1)

def min(arr):
    if len(arr) == 0:
        return None
    return arr[0]

def delete_min(arr):
    if len(arr) == 0:
        return None

    _swap(arr, 0, len(arr)-1)
    min = arr.pop()
    _siftdown(arr, 0, len(arr)-1)

    return min

def _swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def _lchild(parent):
    return 2*parent+1

def _rchild(parent):
    return 2*parent+2

def _parent(child):
    return (child-1)//2

def _siftup(arr, child):
    while _parent(child) >= 0:
        if arr[_parent(child)] <= arr[child]:
            return
        else:
            _swap(arr, _parent(child), child)
            child = _parent(child)

def _siftdown(arr, parent, end):
    while _lchild(parent) <= end:
        minchild = _lchild(parent)

        if (_rchild(parent) <= end) and \
            arr[_rchild(parent)] < arr[_lchild(parent)]:
            minchild = _rchild(parent)

        if arr[parent] > arr[minchild]:
            _swap(arr, parent, minchild)
            parent = minchild
        else:
            break

if __name__ == "__main__":
    arr = [-1, 3, 4, 1, 9, 0, 3, 2]
    heapify(arr)
    print(arr)







