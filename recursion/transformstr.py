
def _transform(txt, i, slate, result):
    if i >= len(txt):
        result.append(str(slate))
        return

    _transform(txt, i+1, slate+txt[i], result)
    if txt[i].isalpha():
        _transform(txt, i+1, slate+txt[i].swapcase(), result)


def _transforma(txt, i, slate, result):
    if i >= len(txt):
        result.append(''.join(slate))
        return

    slate[i] = txt[i]
    _transforma(txt, i+1, slate, result)
    if txt[i].isalpha():
        slate[i] = txt[i].swapcase()
        _transforma(txt, i+1, slate, result)


def _transform_txt(txt, i, result):
    if i >= len(txt):
        result.append(''.join(txt))
        return

    _transform_txt(txt, i+1, result)
    if txt[i].isalpha():
        txt[i] = txt[i].swapcase()
        _transform_txt(txt, i+1, result)


def transform(txt):
    result = []
    slate = [None for s in txt]
    _transforma(txt, 0, slate, result)
    print(result)
    result1 = []
    _transform_txt(list(txt), 0, result1)
    print(result1)


transform("Ab1")
transform("xbAb1")
transform("111")
transform("")
