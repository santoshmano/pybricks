
"""
Problem: Sort array of integers using insertion, bubble and selection sort

input: array of integers, there may be duplicates
output: sorted array
"""

"""
insertion sort:

Return if array len is less than 2.

For every item from index 1 to end of string.
    compare item with the left sorted array
    if item is less then slide the sorted array to right
    insert the item at the correct index
"""

def insertion_sort(arr):
    if len(arr) < 2:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > key:
                arr[j+1] = arr[j]
            else:
                j += 1
                break
        arr[j] = key
    return arr

"""
bubble sort

i from len-1 to 0
    j from 0 to i
        comp and swap j, j+1
"""

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):

    if len(arr) < 2:
        return arr

    for i in range(len(arr)-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

    return arr


"""
selection sort

"""
def selection_sort(arr):

    return arr

if __name__ == "__main__":

    all_sorts = [selection_sort, insertion_sort, bubble_sort]

    for sort in all_sorts:
        lists = [[],
                 [3, 0],
                 [3, 2, 1],
                 [9, 5, 8, 2],
                 [-2, 4, 1, 1, 0, 8, 9]]

        for list in lists:
            print(sort(list), str(sort).sp)




