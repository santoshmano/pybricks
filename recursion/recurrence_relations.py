
# Problem - print permutations of 0/1 , Binary sequences of length n
#
# At each position there are 2 choices
#
# Recurrence Relation
# T(n) = T(n-1) + T(n-1)
#      = 2 * T(n-1)
# T(1) = 2
#
# Time Complexity - O(2**n) #TODO confirm this
# Space Complexity -

## Problem - print permutations of 0/1 , Binary sequences of length n
## without consecutive 0's
#
# At a single position there are 2 choices
#   - remaining subset is N-1
# With 2 positions there are 3 choices
#   - remaining subset is N-2
#
# Recurrence Relation
# T(n) = T(n-1) + T(n-2)
# T(1) = 2  # 0/1
# T(2) = 3  # 01 10 11
#
# Time Complexity - O(??) #TODO check this
# Space Complexity -
#

## Problem - Climb n steps to get a prize.
## At every position you can jump 1 or 2 steps
#
# At a single position there are 2 choices
# jump 1 step or jump 2 steps.
#
# If you jump 1 step
#   - remaining subset is n-1
# If you jump 2 steps
#   - remaining subset is n-2
#
# Recurrence Relation
# T(n) = T(n-1) + T(n-2)
# T(1) = 1  # can jump only 1 step
# T(2) = 2  # can jump 1 + 1 steps, or directly with 2step jump
#
# Time Complexity - O(??) #TODO check this
# Space Complexity -


## Problem - Choosing a subset - choose K items from N
#
# For every item in the set, you can either choose it or not.
#
# T(n, k) = T(n-1, k-1) + T(n-1, k)
#
# T(n,0) = 1
# T(n,n) = 1
#
# eg - T(n,1) = n



