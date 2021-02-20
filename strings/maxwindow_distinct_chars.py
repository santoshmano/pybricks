def longest_distinct_chars(txt, k):

	sofar = {}
	distinct = 0
	start = 0
	end = 0
	window = [0, 0]

	while start < len(txt) and end < len(txt):
		#print(start, end, distinct, sofar, window)
		if distinct <= k:
			c = txt[end]
			if c in sofar:
				sofar[c] += 1
			else:
				sofar[c] = 1

			end += 1
			if sofar[c] == 1: distinct += 1

		while (start < len(txt)-k) and distinct > k:
			#print(start, end, distinct, sofar, window)

			c = txt[start]
			sofar[c] -= 1

			start += 1
			if sofar[c] == 0: distinct -= 1

		if distinct == k:
			if window[0] < end-start+1:
				window[0] = end-start
				window[1] = start

	return window[0], window[1], txt[window[1]:window[1]+window[0]]


print(longest_distinct_chars("eceba", 2))

print(longest_distinct_chars("aabhhcbbaabbbbbbada", 2))
