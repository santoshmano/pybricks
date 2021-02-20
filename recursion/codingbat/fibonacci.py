"""
N Fibonacci numbers
"""

def print_n_fibonacci_i(n):

    fib = 0
    i = 0
    j = 1
    print("Printing N Fibonacci numbers: ")
    if n == 1:
        print(i)
        return
    elif n == 2:
        print(i, j)
        return
    else:
        print (i, j, end=' ')
        for iter in range(2, n):
            fib = i + j
            print(fib, end=' ')
            i = j
            j = fib
    return

def print_n_fibonacci(n):
    for i in range(0,n):
        print(fibonacci(i))

def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print_n_fibonacci(5)