"""
for every element i
    find 2sum between i+1 to end, where target is target-arr[i]
"""
def two_sum(arr, start, end, target):
    left = start
    right = end
    result = []
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            yield (left, right)
            left += 1
            right-=1
            while left<right and arr[left] == arr[left-1]:
                left += 1
            while left<right and arr[right] == arr[right+1]:
                right -= 1
        elif sum < target:
            left += 1
        else:
            right -= 1

    return result

def _print_triplets(arr, target):
    result = []
    end = len(arr)-1
    i = 0
    while i <= end-2:
        twosum = two_sum(arr, i+1, end, target-arr[i])
        for x in twosum:
            result.append((arr[i], arr[x[0]], arr[x[1]]))
        i += 1
        while (i <= end-2) and (arr[i] == arr[i-1]):
            i+=1
    return result

def print_triplets(arr):
    arr.sort()
    result = _print_triplets(arr, 0)
    for x in result:
        print("{},{},{}".format(x[0], x[1], x[2]))

print_triplets([-1, -1, 0, 3, -5, 2, 6, 1, -4, 5, 8, -8])
