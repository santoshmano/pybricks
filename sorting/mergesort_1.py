def mergesort(nums):
    aux = [None for x in nums]
    print("before mergesort - ", nums)
    _mergesort(nums, aux, 0, len(nums)-1)
    print("after mergesort --  ", nums)


def _mergesort(nums, aux, start, end):

    if start >= end:
        return

    mid = start + (end - start) // 2
    print(start, mid, end)
    _mergesort(nums, aux, start, mid)
    _mergesort(nums, aux, mid + 1, end)

    left = start
    right = mid + 1
    auxi = start
    print(left, right, auxi)
    while left <= mid and right <= end:
        if nums[left] <= nums[right]:
            aux[auxi] = nums[left]
            left += 1
        else:
            aux[auxi] = nums[right]
            right += 1
        auxi += 1

    while left <= mid:
        aux[auxi] = nums[left]
        left += 1
        auxi += 1

    while right <= mid:
        aux[auxi] = nums[right]
        right += 1
        auxi += 1

    for i in range(start, end + 1):
        nums[i] = aux[i]


mergesort([34, 2, 1, 23, 12])
