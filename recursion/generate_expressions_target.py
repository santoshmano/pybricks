
# 0505
#
# 0

def gen(s, target):

    result = []

    def _gen(txt, txt_i, prevnum, total, expr):

        if txt_i == len(txt):
            if total == target:
                result.append("".join(expr))
            return

        for end in range(txt_i+1, len(txt)+1):
            curstr = txt[txt_i:end]
            curnum = int(curstr)

            if txt_i:
                _gen(txt, end, curnum, (total-prevnum)+(prevnum*curnum),expr+"*"+curstr)
                _gen(txt, end, curnum, total+prevnum, expr+"+"+curstr)
            else:
                _gen(txt, end, curnum, total, expr+curstr)

        return

    _gen(s, 0, 0, 0, "")

    return result

result = gen("050505", 5)

for expr in result:
    print(expr)
