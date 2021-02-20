
# ipow can be negative or positive.
def pow(num, ipow):
    if ipow == 0:
        return float(1)
    elif ipow > 0:
        return (1 * num) * (pow(num, ipow - 1))
    elif ipow < 0:
        return round((1 / num) * pow(num, ipow + 1), 9)

# faster solution, with memoization
def _pow_mem(num, ipow, cache):
    if ipow in cache:
        return cache[ipow]

    if ipow == 0:
        cache[ipow] = float(1)
    if ipow == 1:
        cache[ipow] = float(num)
    else:
        cache[ipow] = _pow_mem(num, ipow//2, cache) * _pow_mem(num, (ipow - ipow//2), cache)

    return cache[ipow]

def pow_mem(num, ipow):
    cache = {}
    if ipow < 0:
        return round(1 / _pow_mem(num, (ipow*-1), cache), 9)
    else:
        return _pow_mem(num, ipow, cache)

print(pow(10, 3), pow_mem(10, 3))
print(pow (4.5, -3), pow_mem(4.5, -3))
print(pow (9, 0), pow_mem(9, 0))