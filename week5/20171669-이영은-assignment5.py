def iterfibo(n):
    a = 0
    b = 1
    for i in range(n):
        old_a = a
        a = b
        b = old_a + b
    return a


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


import time
import random

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    
