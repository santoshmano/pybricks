"""
Sum Zero
Given a set of integers, find a contiguous subset whose sum is zero.
There can be duplicate numbers in the input.

Input: Integer array e.g. 5,1,2,-3,7,-4
output: A subset that sums to zero.
e.g. 1,2,-3 OR -3,7,-4

* If there are no such subsets, then print nothing
* If there are multiple such subsets, then print any one
* If a matching subset is a subset of a larger matching subset, then print
* either one. If there is a number '0' in the array, then it counts as a
* valid answer sub-array.
"""

# Naive O(n**2) solution
# start from index 0 and traverse through the array to find a contiguous
#   sub-array which adds to zero
# repeat the above for every index till we find a suitable sub-array

def sum_zero_1(a):
    results = []
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum == 0:
                results.append([a[i] for i in range(i, j + 1)])
    return results

def sum_zero(arr):

    results = []
    sum_map = {} # sum at index (sum, index) mapping

    sum = 0

    for i in range(len(arr)):

        sum += arr[i]

        if sum == 0:
            #found zero sum sub-array from 0 to i
            results.append([arr[i] for i in range(0, i+1)])

        if sum in sum_map:
            for j in range(0, len(sum_map[sum])):
                results.append([arr[i] for i in range(sum_map[sum][j]+1, i+1)])

        if sum in sum_map:
            sum_map[sum].append(i)
        else:
            sum_map[sum] = [i]

    return results


print(sum_zero([5,1,2,-3,7,-4]), sum_zero_1([5,1,2,-3,7,-4]))
print(sum_zero([5,1,2,3,7,4]), sum_zero_1([5,1,2,3,7,4]))
print(sum_zero([5,1,2,0,7,-4]), sum_zero_1([5,1,2,0,7,-4]))
print(sum_zero([0,1,2,3,4,-10]), sum_zero_1([0,1,2,3,4,-10]))
print(sum_zero([0, 4, 0, 1, 2, -3]), sum_zero_1([0, 4, 0, 1, 2, -3]))
print(sum_zero([3, 1, 2, 3]), sum_zero_1([3, 1, 2, 3]))
print(sum_zero([5,1,2,5,-7,10]), sum_zero_1([5,1,2,5,-7,10]))
print(sum_zero([0, 0]), sum_zero_1([0, 0]))
