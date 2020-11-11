def fib(num):
    # return n-th Fibonacci number
    if num in (0, 1):
        return num
    else:
        return fib(num-1) + fib(num-2)
