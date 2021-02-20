
# Array Product
# Given an array store in the array[i] the product of all the numbers of the array other than i.
#
# example
# input : [1, 2, 3, 4, 5]
# output: [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]
#          = [120, 60, 40, 30, 24]
#
# Do this in O(1) solution without using division

# naive O(n**2) solution
def array_product2(arr):
    """
    :param arr: input array of integers
    :return: product array
    """

    prod_arr = [1 for _ in range(0, len(arr))]

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if j == i:
                continue
            else:
                prod_arr[i] *= arr[j]

    return prod_arr


#O(n) solution with 2 iterations and using division

def array_product3(arr):

    prod_arr = [1 for _ in range(0, len(arr))]
    prod = 1
    for i in range(0, len(arr)):
        prod *= arr[i]

    for i in range(0,len(arr)):
        prod_arr[i] = int(prod/arr[i])

    return prod_arr

# O(n) solution without division
# a[i] = a[0]*a[1]....*a[i-1] *
#            a[i+1]*....a[n-2]*a[n-1]

def array_product(arr):
    prod_arr = [1 for _ in range(0, len(arr))]
    forward_prod = 1
    for i in range(0, len(arr)):
        forward_prod *= arr[i]
        prod_arr[i] = forward_prod/arr[i]

    backward_prod = 1
    for i in range(len(arr)-1, -1, -1):
        backward_prod *= arr[i]
        prod_arr[i] = prod_arr[i] * (backward_prod/arr[i])

    return prod_arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    print(array_product2(arr))
    print(array_product3(arr))
    print(array_product(arr))

