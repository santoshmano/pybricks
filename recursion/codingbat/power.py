def power(base, exp):
    result = 1
    for i in range(0, exp):
        result *= base

    return result


print(power(2, 0))
print(power(2, 3))
print(power(2, 5))
