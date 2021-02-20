

def _subset(nums, i, sub, result):
    if i >= len(nums):
        result.append(list(sub))
        return

    _subset(nums, i+1, sub, result)
    sub.append(nums[i])
    _subset(nums, i+1, sub, result)
    sub.pop()

def subset(nums):
    result = []
    _subset(nums, 0, [], result)
    print(result)


subset([1, 2, 3])