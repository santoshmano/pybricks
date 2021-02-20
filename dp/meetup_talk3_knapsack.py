"""
Knapsack Problem

Greedy algorithm
Thief wants to figure out what items to get

Weight limit = 100

I = [(val, w), (val, w)…]

ratio = V_item / W_item (value/weight)


example 

Items = [(100, 1), (200, 100)]

v1/w1 = 100 , v2/w2 = 2

so in knapsack problem you just take I1, and no part of I2, So the ratio is not that great. 
So in greedy solution you don’t want walk away with a solution with the bag full. 



Sort by value/weight ratio

[i1, i2, i3, i4, i5……in]

s1. i1 + i2 + i3 legal solution
s2. if we add i4 we will exceed weight limit
so we can choose s1 or s2, we choose s2, which is just i4 

OPT = weight_uses * average value/weight ration

s1 + s2 > optimal solution, that means atleast 1 of them is atleast half of the optimal solution == this is approximation algorithm. 


Polynomial time complexity = O(N^c) N to the power of C  <— this is NP complete problems. 


There are two classes of knapsack problems, values being small, or weights being small. 


Recursive solution:

Say if Items are in a list - i1 i2 i3 ….i 

F(i, w) = 


BruteForce approach is 
 - create all subsets
 - check value for every subset
 - time complexity is 2^N


F (i, C) = F(i+1, C)		if C < A[i].weight
	   otherwise
	   F(i+1, C-A[i].w + A[i].value)


	max ( F(i+1, C-A[i].w + A[i].value), F(i+1, C))

"""
