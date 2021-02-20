'''
0 1 1 2 3 5
nth fibonacci number
https://www.youtube.com/watch?v=RHVkCLWS_T0

DP logic:
    1. check base cases
    2. check cache for answer
    3. compute function normally
    4. write to cache
    5. return ans from (3)
'''

# iterative
def _fib_iter(n):
    if n == 1: return 0
    if n == 2: return 1

    a = 0
    b = 1
    fib = a+b
    for i in range(3, n+1):
        fib = a + b
        a = b
        b = fib

    return fib

# recursive
def _fib(n):
    if n==1: return 0
    if n==2: return 1

    return _fib(n-1) + _fib(n-2)

# with memoization
def _fib_memo(n, cache):
    if n==1:
        cache[n-1] = 0
    if n==2:
        cache[n-1] = 1

    if cache[n-1] == -1:
        cache[n-1] = _fib_memo(n-1, cache) + _fib_memo(n-2, cache)

    return cache[n-1]



def _fib_dp(n, cache):
    if n==1:
        cache[n-1] = 0
    if n==2:
        cache[n-1] = 1

    for i in range(2, n):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[n-1]

"""

# Class notes

# fibonacci

def fib(n)
    return _fib_helper(n, dict())

def _fib_helper(n, dp)
    1. check base cases
    2. check cache for answer
    3. compute function normally
    4. write to cache
    5. return ans from (3)

Check your problem -
 Should be able to write an equation for a problem recursively
 There should be overlapping sub-problems
    if no overlap then we will never use the cache

Memoization:
    - Use dict() when the cache is sparse
    - Can use array if contiguous

Problems can be solved using
    - Dynamic Programming or
    - Divide and Conquer

Binary search - no overlapping sub-problems, so no DP there.
MergeSort - splits the array in half  and sub-problems are completely independent

# Code as explained in talk
# O(n) = # of states * time taken per state
# (time taken per state = all lines other than f(n-1) + f(n-2) which is O(1) ...)
# (state is usually based on input arguments)
# (# of states = usually how many different n's will i call the function with)A
# in multi argument function it may be different - count every combination of the arguments
# for ex i, j usually n**2 or n**3 d
# O(n) - n * O(1)
#
# space complexity = #of states * space per state
"""

def _fib_helper(n, dp):
    if n == 1: return 0
    if n == 2: return 1

    if n in dp:
        return dp[n]

    result = _fib_helper(n-1, dp) + _fib_helper(n-2, dp)
    dp[n] = result

    return result


def fib(n):
    if n<1:
        return -1
    cache = [-1 for _ in range(n+1)]
    print("Fib({:3}) - {:5}, {:5}, {:5}, {:5}, {:5}".format(
            n,
            _fib(n),
            _fib_iter(n),
            _fib_memo(n, cache),
            _fib_dp(n, cache)),
            _fib_helper(n, dict()))

if __name__ == "__main__":
    for i in range(1,20):
        fib(i)


