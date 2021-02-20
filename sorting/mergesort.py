
"""
Divide the array into two halves
Sort them individually
Merge the two sorted arrays
"""
def merge(a, aux, start, mid, end):
    left = start
    right = mid+1

    for i in range(0, len(a)):
        aux[i] = a[i]

    i = start
    while left <= mid and right <= end:
        if aux[left] <= aux[right]:
            a[i] = aux[left]
            left += 1
        else:
            a[i] = aux[right]
            right += 1
        i += 1

    while left <= mid:
        a[i] = aux[left]
        left += 1
        i += 1

    while right <= end:
        a[i] = aux[right]
        right += 1
        i += 1

def _merge_sort(a, aux, start, end):
    if start >= end:
        return
    mid = (start+end)//2
    _merge_sort(a, aux, start, mid)
    _merge_sort(a, aux, mid+1, end)
    merge(a, aux, start, mid, end)

def merge_sort(a):
    aux = [x for x in a]
    _merge_sort(a, aux, 0, len(a)-1)

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
        merge_sort(a)
        print("After:", a)

