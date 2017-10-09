import time

def iterfibo(n):
    a1 = 0
    a2 = 1
    answer = 1
    
    if n == 0 :
        answer = a1
    #elif n == 1 :
    #    answer = a2
    else:
        for i in range(0,n-1):
            answer = a1 + a2
            a1 = a2
            a2 = answer
    return answer

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
while True:
    n=int(input("n :"))
    if n == -1:
        break

    time1 = time.time()
    answer1 = iterfibo(n)
    time2 = time.time()
    iter_time = time2 - time1

    time3 = time.time()
    answer2 = fib(n)
    time4 = time.time()
    fib_time = time4 - time3

    print("iter :",iter_time,"\nfibo :",fib_time)
    


