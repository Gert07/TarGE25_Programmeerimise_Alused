
def fibo_tail(n, fib, prev):
    if n == 1: return prev
    return fibo_tail(n - 1, fib + prev, fib)

print(fibo_tail(100, 1, 1))