# Given an array, sort it using mergesort


def merge(a, start, mid, end, aux):

	for i in range(len(a)):
		aux[i] = a[i]

	left = start
	right = mid+1
	i = left

	while left <= mid and right <= end:
		if aux[left] < aux[right]:
			a[i] = aux[left]
			left += 1
			i += 1
		else:
			a[i] = aux[right]
			right += 1
			i += 1


	while left <= mid:
		a[i] = aux[left]
		i+= 1
		left += 1

	while right <= end:
		a[i] += aux[right]
		right += 1
		i += 1


def _mergesort(a, start, end, aux):
	if end > start:
		mid = (start+end)//2
		_mergesort(a, start, mid, aux)
		_mergesort(a, mid+1, end, aux)
		merge(a, start, mid, end, aux)


def mergesort(a):
	aux = [x for x in a]
	_mergesort(a, 0, len(a)-1, aux)


if __name__ == "__main__":
	arrays = []
	arrays.append([])
	arrays.append([3, 1])
	arrays.append([1])
	arrays.append([4, 1, -4, 5, 1, 6, 7, 9, -10])
	arrays.append([0, 0, 0, 0])

	for array in arrays:
		mergesort(array)
		print(array)