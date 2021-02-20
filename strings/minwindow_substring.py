import sys

def minwindow_substring(S, T):
    st, en, target, window = 0, 0, 0, 0
    hash_tar, hash_win = {}, {}
    for c in T:
        if c not in hash_tar: hash_tar[c] = 1
        else:                 hash_tar[c] += 1
        if c not in hash_win: hash_win[c] = 0
    target = len(T)
    window = sys.maxsize
    window_start = -1
    window_end = -1

    while st < len(S) and en < len(S):
        if target > 0:
            c = S[en]
            if c in hash_tar:
                hash_win[c] += 1
                if hash_win[c] <= hash_tar[c]:
                    target -= 1
            en += 1

        while target == 0:
            if window > en-st+1:
                window = en-st+1
                window_start = st
                window_end = en

            c = S[st]
            if c in hash_tar:
                hash_win[c] -= 1
                if hash_win[c] < hash_tar[c]:
                    target += 1
            st += 1

    if window == sys.maxsize:
        return ""
    else:
        return S[window_start:window_end+1]

def  MinWindow(strText, strCharacters):
    return minwindow_substring(strText, strCharacters)

print(MinWindow("this is a test string", "tist"))
print(MinWindow("caaec", "ace"))
