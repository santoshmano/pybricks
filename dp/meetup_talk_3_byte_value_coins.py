"""
Bytelandion Coins , sphere online judge


Take a coin of value N and exchange it for N/2 , N/3, N/4

For ex = 7 -> 3, 2, 1

Can convert them to dollars.

What is the best exchange rate

N/2 + N/3 + N/4 = 13N/12 > N

(observation - For any N greater than 36 you get a better exchange rate)

But because of truncation we will lose value.

- are there overlapping sub-problems
- decide whether to do bottom up or top down.

F(N) = max(N, F(N/2)+F(N/3)+F(N/4))
F(0) = 0

Draw the tree, to find overlapping sub-problems
exponential

Time complexity:
 Of recursive solution
  - O(3**lgN)
  Space = lgN

 Top down DP solution
  (number of states is not obvious, as we may
   Time
   = No of states * time taken per state.
   =

   Space Complexity
    = O(Number of states)

 Bottom UP
   Compute all of F{0) , F(1) F(2) and then
   Time - O(N)
   Space - O(N)


   N / (2**i * 3**j)

   F(i, j) = max(

"""

# recursive solution
def xch(N):
   if N == 0:
      return 0

   return max(N, xch(N//2)+xch(N//3)+xch(N//4))


# top down dynamic
def xch_td(N, cache):
   if N == 0:
      return 0

   if N in cache:
      return cache[N]

   result = max(N, xch_td(N//2)+xch_td(N//3)+xch_td(N//4))
   cache[N] = result

   return result

# bottup up
def xch_bu(N, cache):
   if N == 0:
      return 0

   for i in range(0  , N+1):
      cache[i] = max(i, cache[i//2]+cache[i//3]+cache[i//4])

   return cache[N]


