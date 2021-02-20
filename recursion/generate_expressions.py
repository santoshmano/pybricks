

def gen(s, target):

    result = []
    if not s: return result

    def _gen0(txt, txt_i, expr):

        if txt_i == len(txt):
            result.append("".join(expr))
            return

        for end in range(txt_i+1, len(txt)+1):
            nextstr = txt[txt_i:end]
            nextnum = int(nextstr)

            if txt_i:
                _gen0(txt, end, expr+"*"+nextstr)
                _gen0(txt, end, expr+"+"+nextstr)
            else:
                _gen0(txt, end, expr+nextstr)

        return

    def _gen1(txt, txt_i, expr):

        if txt_i == len(txt):
            result.append("".join(expr))
            return

        _gen2(txt, txt_i+1, expr+txt[txt_i])
        _gen2(txt, txt_i+1, expr+"*"+txt[txt_i])
        _gen2(txt, txt_i+1, expr+"+"+txt[txt_i])

        return


    def _gen2(txt, txt_i, expr):
        if txt_i == len(txt):
            result.append("".join(expr))
            return

        _gen2(txt, txt_i+1, expr+txt[txt_i])

        if not txt_i:
            return
        _gen2(txt, txt_i+1, expr+"*"+txt[txt_i])
        _gen2(txt, txt_i+1, expr+"+"+txt[txt_i])

        return

    def _gen3(txt, txt_i, expr):

        if txt_i == len(txt):
            result.append("".join(expr))
            return

        expr.append(txt[txt_i])
        _gen3(txt, txt_i+1, expr)
        expr.pop()

        expr.append("*")
        expr.append(txt[txt_i])
        _gen3(txt, txt_i+1, expr)
        expr.pop();
        expr.pop();

        expr.append("+")
        expr.append(txt[txt_i])
        _gen3(txt, txt_i+1, expr)
        expr.pop()
        expr.pop()

        return


    #_gen0(s, 0, "")
    #_gen1(s, 1, s[0])
    #_gen2(s, 0, "")
    _gen3(s, 1, [s[0]])

    return result

result = gen("050505", 5)

for expr in result:
    print(expr)
