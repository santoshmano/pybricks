# Print all subsets of a given string/array
#
# For every element in the string choose it or not
#   - repeat above for every resulting substring
#
# Recurrence Relation
# AllSubsetsOf(a[i...n-1]) =
#  {} if i == n
#  AllSubsets{a[i+1..n]} + AllSubsets{a[i+1...n] plus a[i]}
#
# Time Complexity - O(2^n)
# Space Complexity -
#

# string version
def _subsets_print2(sub_s, orig_s):
    if len(orig_s) == 0:
        print(sub_s)
        return
    _subsets_print2(sub_s, orig_s[1:])
    _subsets_print2(sub_s+orig_s[0], orig_s[1:])
# array version
def _subsets_print(so_far, rest):
    if not rest:
        print(so_far)
    else:
        _subsets_print(so_far + [rest[0]], rest[1:])
        _subsets_print(so_far, rest[1:])

# array version with indices
def _subsets_print3(inp, i, out, o):
    if i == len(inp):
        """
        for i in out:
            if i is not None:
                print(i, end=" ")
        print()
        """
        print(out)
        return

    out.append(inp[i])
    #out[o] = inp[i]
    _subsets_print3(inp, i+1, out, o+1)
    #out[o] = None
    out.pop()
    _subsets_print3(inp, i+1, out, o)

def subsets_print(string):
    arr = [1, 2, 3, 4]
    #_subsets_print([], arr)
    #_subsets_print2("", string)
#    _subsets_print3(arr, 0, [None for _ in range(len(arr))], 0)
    _subsets_print3(arr, 0, [], 0)

s = "1234"
subsets_print(s)
