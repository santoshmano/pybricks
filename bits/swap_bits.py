def swap_bits(num, i, j):
    if (num>>i & 1) != (num>>j & 1):
        num ^= ((1<<i) | (1<<j)) 
    return num

num = 129

for x in range(num, num+10): 
    print(bin(x), bin(swap_bits(x, 1, 2)))
