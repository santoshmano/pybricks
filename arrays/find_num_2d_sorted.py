"""
Find a number in a 2D sorted array with (n x m) n rows, m columns
"""

# binary search the right row which may have the num
# binary search the columns within the 1 row to find the num
# Time complexity log(n) + log(m)
#
def find_num_2d_sorted(arr, num):
    i, j = None, None
    found = False

    # binary search the containing row

    low = 0
    high = len(arr)-1
    containing_row = None

    while low <= high:

        mid = (low + high) // 2

        if num < arr[mid][0]:
            high = mid-1
        elif num > arr[mid][len(arr[0])-1]:
            low = mid+1
        else:
            containing_row = mid
            break

    if containing_row == None:
        return found, i, j

    # found the row, binary search the col

    low = 0
    high = len(arr[0])-1

    while low <= high:

        mid = (low + high) // 2

        if num < arr[containing_row][mid]:
            high = mid-1
        elif num > arr[containing_row][mid]:
            low = mid+1
        elif num == arr[containing_row][mid]:
            found = True
            i = containing_row
            j = mid
            break

    return found, i,j


arr = [[ 2,  4,  8,  9],
       [12, 14, 17, 19],
       [20, 23, 25, 28],
       [31, 37, 38, 39],
       [44, 49, 49, 49]]

for num in range(10,30):
    print(num, ":", find_num_2d_sorted(arr, num))