# TODO: do o(n*2) solution as

def shortest(txt, chars_set):
    count = len(chars_set)
    shortest_length = float('inf')
    shortest_pair = (0,0)
    chars_hash = {}

    for c in chars_set:
        chars_hash[c] = 0

    l = 0; r = 0

    while (l < len(txt)) and (r < len(txt)):

        # advance right till we find all elements
        while count and r < len(txt):
            if txt[r] in chars_hash:
                if not chars_hash[txt[r]]:
                    count -= 1
                chars_hash[txt[r]] += 1
            r += 1

       # advance left to compress the substring
        while l<=r:
            if txt[l] in chars_hash:
                if chars_hash[txt[l]] == 1:
                    break
                chars_hash[txt[l]] -= 1

            l += 1

        if not count:
            # if we found all elems, reset window
            if (r-l) < shortest_length:
                shortest_length = r-l
                shortest_pair = (l,r)
        else:
            # else we do not have a window break out
            break

        chars_hash[txt[l]] -= 1
        count -= 1
        l += 1

    return txt[shortest_pair[0]:shortest_pair[1]+1]


print(shortest("hellodarknessmybestfriend", set(['e', 'r'])))
print(shortest("hellodarknessmybestfriend", set(['e', 'r', 'd'])))
print(shortest("hellodarknessmybestfriend", set(['h', 's'])))
print(shortest("hellodarknessmybestfriend", set(['h', 'l', 'l'])))

