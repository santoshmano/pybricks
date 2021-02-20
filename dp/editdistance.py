def diffBetweenTwoStrings(source, target):
    """
    @param source: str
    @param target: str
    @return: str[]
    """
    si = 0
    ti = 0
    totalResults = []
    cur = ["T"]

    _diff(source, target, si, ti, totalResults, cur)


    bestRes = 1000000
    for res in totalResults:
        print(len(res))
        if len(res) < bestRes:
            finalRes = res
            bestRes = len(res)

    print(len(finalRes), len(totalResults))
    return finalRes


def _diff(src, tgt, si, ti, totalResults, cur):
    #print(cur)
    #print(cur, src, tgt, si, ti)
    if si >= len(src) and ti >= len(tgt):
        totalResults.append(cur)
        return
    elif si == len(src):
        cur.append("+" + str(tgt[ti]))
        _diff(src, tgt, si, ti + 1, totalResults, cur)
    elif ti == len(src):
        cur.append("-" + str(src[si]))
        _diff(src, tgt, si + 1, ti, totalResults, cur)
    else:
        #print(cur, src, tgt, si, ti)
        if src[si] == tgt[ti]:

            cur.append(src[si])
            _diff(src, tgt, si + 1, ti + 1, totalResults, cur)
            #_diff(src, tgt, si + 1, ti + 1, totalResults, cur+str(src[si]))
        else:
            opt1 = cur
            opt2 = cur
            opt1.append("-" + str(src[si]))
            opt2.append("+" + str(src[si]))

            _diff(src, tgt, si + 1, ti, totalResults, opt1)
            _diff(src, tgt, si, ti + 1, totalResults, opt2)


diffBetweenTwoStrings("ABCEDFG", "ABDFFGH")