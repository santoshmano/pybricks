"""
ind     0  1   2  3   4
nums = [9  10  2  3  1]

out    in
1      0-0
2      1-0
3      2-1

n-1      (n-1)-0
"""


def bubble_sort(nums):
    for i in range(len(nums), 0, -1):
        for j in range(1, i):
            if nums[j] < nums[j-1]:
                # swap
                nums[j], nums[j-1] = nums[j-1], nums[j]


def selection_sort(nums):
    for i in range(0, len(nums)):
        smallest = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        x = nums[i]
        j = i
        while (j > 0) and nums[j-1] > x:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = x


def quick_sort(nums):
    _quick_sort(nums, 0, len(nums)-1)


def _quick_sort(nums, start, end):
    if start < end:
        pivot = partition(nums, start, end)
        _quick_sort(nums, start, pivot-1)
        _quick_sort(nums, pivot+1, end)

import random

def partition(nums, start, end):
    pivot = random.randint(start,end)
    nums[start], nums[pivot] = nums[pivot], nums[start]
    left = start+1
    right = end
    while left <= right:
        if nums[left] <= nums[start]:
            left += 1
        elif nums[right] >= nums[start]:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]

    nums[start], nums[right] = nums[right], nums[start]

    return right

numsarray = \
    [[9, 3, 0, 1, 2],
     [-1, -123, 0, 1213, 99],
     [1, 1, 2, 1, 0],
     [23, 1, 12, 12, 12],
     [0, 0, 0],
     [],
     [1]]

for nums in numsarray:
    print(nums)
    quick_sort(nums)
    print(nums)
