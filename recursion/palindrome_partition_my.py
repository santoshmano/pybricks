
def is_palindrome(s):
    if len(s) <= 1:
        return True

    if (s[0] != s[-1]):
        return False

    return is_palindrome(s[1:-1])

def pal_dec(s, i, results):
    if i == len(s):
        print(results)
        return

    for n in range (i, len(s)):
        if (is_palindrome(s[i:n+1]) == True):
            results.append(s[i:n+1])
            pal_dec(s, n+1, results)
            results.pop()

def pal_dec_M(s):
    results = []
    pal_dec(s, 0, results)
    print(results)



pal_dec_M("abaa")
pal_dec_M("aaaa")
'''
pal_dec_M("a")
pal_dec_M("")
pal_dec_M("abaaba")
pal_dec_M("malayalam")
pal_dec_M("hindi")
'''


''''
# Complete the function below.

def is_palindrome(s):
    if len(s) <= 1:
        return True

    if (s[0] != s[-1]):
        return False

    return is_palindrome(s[1:-1])

def print_string(results):
    for i in results:
        print(str(i),end='')
        print("|", end='')
    print("")

def _palindromicDecomposition(s, i, results):
    if i == len(s):
        print_string(results)
        return

    for n in range (i, len(s)):
        if (is_palindrome(s[i:n+1]) == True):
            results.append(s[i:n+1])
            _palindromicDecomposition(s, n+1, results)
            results.pop()

def palindromicDecomposition(strInput):
    results = []
    _palindromicDecomposition(strInput, 0, results)
'''