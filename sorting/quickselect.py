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

def _quickselect(arr, start, end, k):
    pivot = _partition(arr, start, end)

    if pivot == k-1:
        return arr[pivot]

    if k-1 < pivot:
        return _quickselect(arr, start, pivot-1, k)
    elif k-1 > pivot:
        return _quickselect(arr, pivot+1, end, k)


def quickselect(arr, k):
    if k < 1 or k > len(arr):
        return None
    return _quickselect(arr, 0, len(arr)-1, k)

if __name__ == "__main__":
    arr = []
    arr.append(([3, 4, 1, 21, 5, 1, 7], 5))
    arr.append(([13, 521, 12, 4, 14, 55, 13, 5, 11, 52], 3))
    arr.append(([], 0))
    arr.append(([1], 1))
    arr.append(([4, 1], 2))
    arr.append(([1, 5], 1))
    arr.append(([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 5))
    arr.append(([1, 3, 2], 3))
    arr.append(([1, 1, 1], 2))
    arr.append(([0, 0, 0, 0, 0, 0, 0, 0], 7))

    for a in arr:
        print("Element {} in {} is {}".format(a[1], a[0], quickselect(a[0], a[1])))
