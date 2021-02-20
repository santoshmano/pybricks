
"""
Problem below is i did not know what is the return, 
	return list of items  or return maximum 
def knapsack(items,
			 cur_items_index,
			 capacity,
			 weights,
			 profits,
			 cur_items,
			 cur_profit,
			 cur_weight,
			 max_items,
			 max_profit):

	if (cur_items_index > len(items)-1) or \
		cur_weight < capacity:
		return 
	
"""


def knapsack(w, p, c):
	return _knapsack(w, p, c, 0)


def _knapsack(w, p, c, i):
	if i >= len(w) or c <= 0:
		return 0

	p1 = p[i] + _knapsack(w, p, c-w[i], i+1)
	p2 = _knapsack(w, p, c, i+1)

	return max(p1, p2)


def knapsack_memo(w, p, c):
	memo = [[None for _ in range(c+1)] for _ in range(len(w))]
	return _knapsack_memo(w, p, c, 0, memo)


def _knapsack_memo(w, p, c, i, memo):
	if i >= len(w) or c <= 0:
		return 0

	p1 = p[i] + _knapsack(w, p, c-w[i], i+1)
	p2 = _knapsack(w, p, c, i+1)
	memo[i][c] = max(p1, p2)

	return memo[i][c]


print(knapsack([2, 3, 1, 4], [4, 5, 3, 7], 5))
print(knapsack_memo([2, 3, 1, 4], [4, 5, 3, 7], 5))

print(knapsack([2, 3, 1, 4, 8], [4, 5, 3, 7, 15], 5))
print(knapsack_memo([2, 3, 1, 4, 8], [4, 5, 3, 7, 15], 5))
