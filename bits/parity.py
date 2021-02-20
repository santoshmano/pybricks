# Compute parity of a given number. 
#   - if the number has odd number of 1's parity is 1
#   - if the number has even number of 1's parity is 0


def parity_1(num):
    parity = 0
    while num:
        if (num & 1):
            parity ^= 1
        # other way of writing the above is below
        # parity ^= num & 1

        num >>= 1
        # other way of writing the above is below
        # num &= num-1
    return parity

def parity_2(num):
    return \
        precomputed_parity_64[num >> (16*3) & MASK_16] ^ \
        precomputed_parity_64[num >> (16*2) & MASK_16] ^ \
        precomputed_parity_64[num >> (16*1) & MASK_16] ^ \
        precomputed_parity_64[num >> (16*0) & MASK_16] 

def parity_3(num):
    num = (num >> 32) ^ num
    num = (num >> 16) ^ num
    num = (num >> 8) ^ num
    num = (num >> 4) ^ num
    num = (num >> 2) ^ num
    num = (num >> 1) ^ num
    return num & 0x1

MASK_16 = 0xFFFF
precomputed_parity_64 = [0 for x in range(0,MASK_16+1)]

for num in range(0, MASK_16+1):
    precomputed_parity_64[num] = parity_1(num)

print(precomputed_parity_64)
for num in range(0,16):
    print("parity of {}-{} is {}".format(num, bin(num), parity_1(num)))
    print("parity of {}-{} is {}".format(num, bin(num), parity_3(num)))
