def count_bits(x):
    count = 0
    while (x):
        if (x & 0x1):
            count += 1
        x = x>>1
    return count

print("bits set in 8 =", count_bits(8))
print("bits set in 1 =", count_bits(1))
print("bits set in 0 =", count_bits(0))
print("bits set in 12 =", count_bits(12))
print("bits set in 15 =", count_bits(15))

