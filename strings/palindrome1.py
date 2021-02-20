
def is_palindrome(s, l, r):
    while (l<r):
        if s[l] != s[r]:
            return False
        l+=1
        r-=1

    return True

# O(n**3) solution
def longest_palindromic_substring(txt):

    # start from longest substring to smallest
    for l in range(len(txt), 0, -1):
        for s in range(0, len(txt)):
            if is_palindrome(txt, s, s+l-1):
                # preempt and return when first found
                return txt[s:s+l]

            if s+l >= len(txt):
                break

    return ""


def longest_palindromic_substring1(txt):

    #longest = (0,0)
    longest_size = 0
    longest_string = ""
    #baab
    #aabc
    #0123

    # process odd sized palindromes
    for c in range(0, len(txt)):
        s=c-1; e=c+1
        while s>-1 and e<len(txt):
            if txt[s] != txt[e]:
                break
            s-=1;e+=1

        s+=1; e-=1
        if e-s+1 > longest_size:
            longest_size = e-s+1
            longest_string = txt[s:e+1]


    # process even sized palindrome
    for c in range(0, len(txt)-1):
        s = c; e=c+1
        while s>-1 and e<len(txt):
            if txt[s] != txt[e]:
                break
            s-=1; e+=1

        s+=1; e-=1
        if e-s+1 > longest_size:
            longest_size = e-s+1
            longest_string = txt[s:e+1]

    #return txt[longest[0]:longest[1])
    return longest_string

print("solution using O(n**3) soln")
print(longest_palindromic_substring("malayalama"))
print(longest_palindromic_substring("12323daad"))
print(longest_palindromic_substring("daaaad"))
print(longest_palindromic_substring("aaaaaadaaaad"))
print(longest_palindromic_substring("asdafdsfdaaaadasd"))

print("solution using O(n**2) soln")
print(longest_palindromic_substring1("malayalama"))
print(longest_palindromic_substring1("12323daad"))
print(longest_palindromic_substring1("daaaad"))
print(longest_palindromic_substring1("aaaaaaadaaaad"))
print(longest_palindromic_substring1("asdafdsfdaaaadasd"))
