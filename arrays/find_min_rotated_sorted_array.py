# Minimum in a rotated-sorted array

# O(n) solution :
# Go through the array to find the first decreasing number.
# If such a number is not found then the first number in array is
# the minimum.
#
# examples
# 1 2 3 4 5
# 4 5 1 2 3
#
def find_minimum_rotated_sorted_1(arr):
    """
    :param arr: rotated sorted array
    :return: minimum and value
    """
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            break

    return min


# O(log(n)) solution. Binary search technique.
def find_minimum_rotated_sorted(arr):
    low = 0
    high = len(arr)-1

    if high < 0:
        return None

    if low == high:
        return arr[0]

    while low <= high:

        mid = (low + high) // 2

        if low < mid and arr[mid] < arr[mid-1]:
            return arr[mid]

        if high > mid and arr[mid] > arr[mid+1]:
            return arr[mid+1]

        # recursive conditions
        if arr[high] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1


print(find_minimum_rotated_sorted([4,1,2,3,4]))