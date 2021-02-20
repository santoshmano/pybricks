def _is_match(txt, t, reg, r):
    if t == len(txt) and r == len(reg):
        return True

    if t != len(txt) and r == len(reg):
        return False

    print(txt,":", t,"  ", reg,":", r)

    if (r+1 < len(reg)) and reg[r+1] == "*":
        return (_is_match(txt, t, reg, r+2)) or \
            (((txt[t] == reg[r]) or (reg[r] == ".")) and _is_match(txt, t+1, reg, r))

    elif (txt[t] == reg[r]) or (reg[r] == "."):
        return _is_match(txt, t+1, reg, r+1)
    else:
        return False

def  isMatch(strText, strPattern):
    return _is_match(strText, 0, strPattern, 0)

if __name__ == "__main__":
    #print(isMatch("kickstart", "hungry"))
    #print(isMatch("aaaaaa", ".a*"))
    print(isMatch("aaa", ".*b"))
