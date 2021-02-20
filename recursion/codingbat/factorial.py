"""
Factorial of N, recursive and iterative
"""

def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def factorial_i(n):

    fact = 1
    for i in range(n, 0, -1):
        fact *= i

    return fact


print("Factorial of N : N!, N!")
for i in range(10, -1, -1):
    print("Factorial of", i, ":", factorial(i), factorial_i(i))

