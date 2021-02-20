def _swap(a, i1, i2):
    a[i1], a[i2] = a[i2], a[i1]

def _partition(a, start, end):
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if a[left] <= a[pivot]:
            left += 1
        elif a[right] >= a[pivot]:
            right -= 1
        else:
            _swap(a, left, right)

    _swap(a, pivot, right)
    return right

def _quicksort(a, start, end):
    if start < end:
        pivot = _partition(a, start, end)
        _quicksort(a, start, pivot-1)
        _quicksort(a, pivot+1, end)

def quicksort(arr):
    _quicksort(arr, 0, len(arr)-1)

if __name__ == "__main__":
    arr = []
    arr.append([3, 4, 1, 21, 5, 1, 7])
    arr.append([13, 521, 12, 4, 14, 55, 13, 5, 11, 52])
    arr.append([])
    arr.append([1])
    arr.append([4, 1])
    arr.append([1, 5])
    arr.append([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    arr.append([1, 3, 2])
    arr.append([1, 1, 1])
    arr.append([0, 0, 0, 0, 0, 0, 0, 0])

    for a in arr:
        print("Before:", a)
        quicksort(a)
        print("After:", a)