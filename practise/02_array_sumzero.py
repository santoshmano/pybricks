# Given a set of integers, find a contiguous subset whose sum is zero.


def sum_zero(arr):

	sum_map = {}
	sum = 0

	for i in range(len(arr)):
		sum += arr[i]

		if sum == 0:
			return [arr[x] for x in range(0, i+1)]

		if sum in sum_map:
			return [arr[x] for x in range(sum_map[sum]+1, i+1)]
		
		sum_map[sum] = i

	return []


print(sum_zero([0]))
print(sum_zero([-1, 1]))
print(sum_zero([-1, 0, 1]))
print(sum_zero([1, 3, 1, 4, 2, -10, 11]))
print(sum_zero([1, -35, 42, 12, -42, -12]))
print(sum_zero([-1, 10]))
