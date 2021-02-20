# Problem - Print permutations of a given string
#
# Recurrence Relation
# T(n) = n * T(n-1)
# T(1) = n
#
# Time Complexity - O(n!)
# Space Complexity -
#

# Array solution
# For each position in the string there are N choices
# Swap it with itself and all the remaining N-1 choices
#   Do the above recursively for each following smaller substring
#
# NOTE - look at for loop - starts from start
def _perm(s, start):
    if start == len(s):
        print("".join(s))
        return
    else:
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            _perm(s, start+1)
            s[start], s[i] = s[i], s[start]

# String solution
# NOTE - look at for loop - starts from 0
def _perm2(perm_s, rem_s):
    if len(rem_s) == 0:
        print(perm_s)

    for i in range(0,len(rem_s)):
        new_perm = perm_s+rem_s[i]
        new_rem = rem_s[0:i]+rem_s[i+1:len(rem_s)]
        _perm2(new_perm, new_rem)

def perm(s):
    print("Permutations of array", s, ":")
    _perm(list(s), 0)
    print("Permutations of string", s, ":")
    _perm2("", s)

# Problem : do not print duplicates
# below takes 0(N!) space solution by storing in hash or set
def _perm2_dup(perm_s, rem_s, set):
    if len(rem_s) == 0:
        if perm_s not in set:
            set.add(perm_s)
            print(perm_s)
        return

    for i in range(0,len(rem_s)):
        new_perm = perm_s+rem_s[i]
        new_rem = rem_s[0:i]+rem_s[i+1:len(rem_s)]
        _perm2_dup(new_perm, new_rem, set)

def perm2_dup(s):
    print("Permutations of string", s, ":")
    _perm2_dup("", s, set())


def _perm2_dup2(perm_s, rem_s):
    if len(rem_s) == 0:
        print(perm_s)
        return

    for i in range(0,len(rem_s)):
        if rem_s[i] in rem_s[i+1:len(rem_s)]:
            continue
        new_perm = perm_s+rem_s[i]
        new_rem = rem_s[0:i]+rem_s[i+1:len(rem_s)]
        _perm2_dup2(new_perm, new_rem)

def perm2_dup2(s):
    print("Permutations of string", s, ":")
    _perm2_dup2("", s)


# Problem - Assume that its an array of integers with half
# the integers even and the other half odd. Print only those
# permutations where odd and even integers alternate,
# starting with odd.

# T(n) = n/2*T(n-2) * n/2*T(n-2)`

def _permutations_odd_even(arr, start, count):

    def num_valid_at_position(num, pos):
        if (num%2==1 and pos%2==0) or (num%2==0 and pos%2==1):
            return True
        else:
            return False

    if start == len(arr):
        #print(arr)
        return count+1

    for i in range(start, len(arr)):
        if num_valid_at_position(arr[i], start):
            arr[start], arr[i] = arr[i], arr[start]
            count = _permutations_odd_even(arr, start+1, count)
            arr[start], arr[i] = arr[i], arr[start]

    return count

# input is 135246
def permutations_odd_even(arr):
    count = _permutations_odd_even(arr, 0, 0)
    print("Total permutations = {0}".format(count))


# Problem: Print all permutations where first k values are odd
# T(n) =   TODO

def _permutations_k_odd(arr, k, start, count):
    def num_valid_at_position(num, pos, k):
        if pos < k and num % 2 == 1:
            return True
        elif pos >= k:
            return True
        else:
            return False

    if start == len(arr):
        print(arr)
        return count+1

    for i in range(start, len(arr)):
        if num_valid_at_position(arr[i], start, k):
            arr[start], arr[i] = arr[i], arr[start]
            count = _permutations_k_odd(arr, k, start+1, count)
            arr[start], arr[i] = arr[i], arr[start]

    return count

# input is 135246
def permutations_k_odd(arr, k):
    count = _permutations_k_odd(arr, k, 0, 0)
    print("Total permutations = {0}".format(count))

# Problem : Assume that the input is an array of characters.
# Print any one permutation that is also a word in the
# dictionary
#
# T(n) =

""" Reference for backtracking
def _perm_first_word(s, start):
    if start == len(s):
        print("".join(s))
        return
    else:
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            _perm_first_word(s, start+1)
            s[start], s[i] = s[i], s[start]

"""
# return: True if first word found in a permutation/False
def _perm_first_word(s, start):

    def is_valid_word(word):
        dict = ["hello", "how", "are", "you", "anjali"]

        if word in dict:
            return True
        else:
            return False

    if start == len(s):
        word = "".join(s)
        if is_valid_word(word):
            print(word)
            return True
        else:
            return False
    else:
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            if (_perm_first_word(s, start+1)):
                return True
            s[start], s[i] = s[i], s[start]

    return False

def perm_first_word(s):
    _perm_first_word(list(s), 0)

# Print up to k permutations that are dictionary words. If
# you are able to find k, return TRUE. Otherwise, print as
# many as you can and return FALSE.
# return: True if k words found in all permutations/False
def _perm_k_words(s, start, k, count):

    def is_valid_word(word):
        dict = ["aanjli", "anjali", "jaanli"]

        if word in dict:
            return True
        else:
            return False

    if start == len(s):
        word = "".join(s)
        if is_valid_word(word):
            print(word)
            return count+1
        else:
            return count
    else:
        for i in range(start, len(s)):
            # for duplicates
            if i > start and s[i] == s[start]:
                continue
            s[start], s[i] = s[i], s[start]
            count = _perm_k_words(s, start+1, k, count)
            if count == k:
                return count
            s[start], s[i] = s[i], s[start]

    return count

def perm_k_words(s, k):
    count = _perm_k_words(list(s), 0, k, 0)
    print("count - ", count)

    return count==k

if __name__ == "__main__":
    s = "appp"
#    perm2_dup2(s)
    s = "appp"
#    perm2_dup(s)
    s = "ABCD"
#    perm(s)

    arr = [[] for x in range(10)]
    arr[0] = []
    arr[1] = [0,1]
    arr[2] = [0,1,2,3]
    arr[3] = [0,1,2,3,4,5]
    arr[4] = [0,1,1,3,4,5]
    arr[5] = [0,1,2,3,4,5,6,7]
    arr[6] = [0,1,2,3,4,5,6,7,8,9]

    for i in 0,1,2,3,4:
        #print("Permutation of {0} elements".format(i*2))
        #permutations_odd_even(arr[i])
        pass
    for i in 3,4:
        #print("Permutation of {0} elements".format(i*2))
        #permutations_odd_even(arr[i])
        #permutations_k_odd(arr[i], 3)
        pass

    perm_first_word("olleh")
    perm_first_word("owh")
    perm_first_word("rea")
    perm_first_word("oyh")
    perm_first_word("oyu")
    perm_first_word("ialjan")
    perm_first_word("ialkan")

    print("count = 6", perm_k_words("ialjan", 6))
    print("count = 3", perm_k_words("ialjan", 3))
    print("count = 2", perm_k_words("ialjan", 2))
    print("count = 1", perm_k_words("ialjan", 1))


