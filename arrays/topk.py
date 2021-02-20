from heapq import *

def topk(nums,k):

	minHeap = []

	#construct heap with k elements first
	for i in range(k):
		heappush(minHeap, nums[i])

	for i in range(k, len(nums):
		if minHeap[0] < nums[i]:
			heappop(minHeap)
			heappush(minHeap, nums[i])

    return list(minHeap)

print(topk([2, 4, 1, 0, 5], 3)
