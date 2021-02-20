def pattern_matcher(text, pattern):
	# Write your code here

    def _match(txt, t, pat, p):

        if t == len(txt) and p == len(pat):
            return True

        if t != len(txt) and p == len(pat):
            return False

        if (p+1 < len(pat)) and (pat[p+1] == "*"):
            noopt = _match(txt, t, pat, p+2)
            if t == len(txt): return False
            if txt[t]==pat[p] or (pat[p]=="."):
                skip1 = _match(txt, t+1, pat, p)
            return noopt or skip1
        elif (pat[p] == "."):
            return _match(txt, t+1, pat, p+1)
        elif t<len(txt) and (pat[p] == txt[t]):
            return _match(txt, t+1, pat, p+1)
        else:
            return False

    return _match(text, 0, pattern, 0)

print(pattern_matcher("aaa", ".*b"))
