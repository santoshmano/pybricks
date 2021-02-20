
def sumofdigits(n):
    if n == 0:
        return 0
    else:
        digit = n%10
        return digit + sumofdigits(n//10)


print(sumofdigits(129))
print(sumofdigits(123456789))