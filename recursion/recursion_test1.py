# Complete the function below.

'''
Given Inputs:
1. An array of integers
2. Target K

Required Output:
Boolean true or false, whether there is a group of integers (may or may not be contiguous)
in the input, that sums to K.

e.g.
Sum({2, 4, 8}, 6) → true
Sum({2, -4, 8}, 1) → false
Sum({2, 4, 8}, 14) → true
Sum({2, 4, 8}, 9) → false

'''

def _group_sum(arr, index, sum, res):
    def sum_of(res):
        sum = 0
        for x in res:
            sum += x
        return sum

    if index == len(arr):
        if sum_of(res) == sum:
            return True
        else:
            return False

    res.append(arr[index])
    if _group_sum(arr, index+1, sum, res):
        return True
    res.pop()

    if _group_sum(arr, index+1, sum, res):
        return True

    return False

def group_sum(arr, sum):
    result = []
    if (_group_sum(arr, 0, sum, result)):
        print("Found a subset for sum", sum, result)
    else:
        print("No subset found for sum", sum)

group_sum([2, 4, 8], 6)
group_sum([2,-4,8], 1)
group_sum([2,4,8], 14)
group_sum([2, 4, 3, 1, -11, -7], -1)
