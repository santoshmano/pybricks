def dot_product(v1, v2):
    i1 = 0
    i2 = 0
    result = 0.0
    while i1 < len(v1) and i2 < len(v2):
        if v1[i1][0] == v2[i2][0]:
            result += v1[i1][1] * v2[i2][1]
            i1 += 1
            i2 += 1
        elif v1[i1][0] > v2[i2][0]:
            i2 += 1
        else:
            i1 += 1

    return result
if __name__ == "__main__":
    v1 = [(0, 2), (1, 4), (5, 6)] # (2,4,0,0,0,6)
    v2 = [(1,3),(2,4),(5,7)] #(0,3,4,0,0,7)
    print(dot_product(v1, v2))
